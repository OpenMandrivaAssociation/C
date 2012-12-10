%define name	C
%define version	0.05
%define release %mkrel 4

%define major
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	Pseudo-interpreter for C syntax
Version: 	%{version}
Release: 	%{release}

Source:		http://labs.cybozu.co.jp/blog/kazuho/archives/c/%{name}-%{version}.tar.bz2
URL:		http://labs.cybozu.co.jp/blog/kazuhoatwork/2006/01/c.php
License:	GPLv2+
Group:		Development/C
BuildRoot:	%{_tmppath}/%{name}-buildroot

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



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.05-4mdv2011.0
+ Revision: 616411
- the mass rebuild of 2010.0 packages

* Mon Jun 22 2009 Jérôme Brenier <incubusss@mandriva.org> 0.05-3mdv2010.0
+ Revision: 388035
- fix license tag

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.05-2mdv2009.0
+ Revision: 220019
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- import C

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed May 24 2006 Austin Acton <austin@mandriva.org> 0.05-1mdk
- initial package
