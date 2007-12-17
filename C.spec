%define name	C
%define version	0.05
%define release %mkrel 1

%define major
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	Pseudo-interpreter for C syntax
Version: 	%{version}
Release: 	%{release}

Source:		http://labs.cybozu.co.jp/blog/kazuho/archives/c/%{name}-%{version}.tar.bz2
URL:		http://labs.cybozu.co.jp/blog/kazuhoatwork/2006/01/c.php
License:	GPL
Group:		Development/C

%description
C (pronounced large-C) is a pseudo-interpreter of the C programming language.

Without the need of manual compilation, developers can rapidly create scripts
or write one-liners using the C programming language that runs at native-code
speed.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_mandir}/man1/*

