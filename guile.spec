Summary:	GNU Extension language
Summary(pl):	GNU Extension language
Name:		guile
Version:	1.3
Release:	5
Copyright:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		ftp://prep.ai.mit.edu/pub/gnu/guile/%{name}-%{version}.tar.gz
Patch0:		guile-libtool.patch
Patch1:		guile-ansi.patch
Patch2:		guile-scm.patch
Patch3:		guile-info.pach
Prereq:		/sbin/install-info
Conflicts:	glibc <= 2.0.7
Requires:	umb-scheme
Buildroot:	/tmp/%{name}-%{version}-root

%description
Guile, a portable, embeddable Scheme implementation written in C. Guile
provides a machine independent execution platform that can be linked in as a
library when building extensible programs.

%description -l pl
Guile jest implementacj± Scheme napisan± w C. 

%package devel
Summary:	Guile's header files, etc.
Summary(pl):	Pliki nag³ówkowe i dokumentacja Guile.
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	m4
Requires:	%{name} = %{version}

%description devel
What's needed to develop apps linked w/ guile

%description -l pl devel
Pliki nag³ówkowe i dokumentacja Guile.

%package static
Summary:	Guile static libraries
Summary(pl):	Biblioteka statyczna Guile
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Guile static library.

%description -l pl static
Biblioteka statyczna Guile

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--enable-dynamic-linking
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/guile/site

make install prefix=$RPM_BUILD_ROOT/usr/

strip $RPM_BUILD_ROOT/usr/lib/*.so.*.*

ln -s ../../lib/umb-scheme/slib $RPM_BUILD_ROOT/usr/share/guile/slib

gzip -9fn $RPM_BUILD_ROOT/usr/info/data-rep* \
	AUTHORS ChangeLog GUILE-VERSION HACKING NEWS README 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/data-rep.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/data-rep.info.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/*.so.*.*
/usr/share/guile

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,GUILE-VERSION,HACKING,NEWS,README}.gz

/usr/include/*
%attr(755,root,root) /usr/lib/*.so

%files static
%defattr(644,root,root,755)
%attr(644,root,root) /usr/lib/*.a

%changelog
* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-5]
- recompiles on new rpm.

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-4]
- added "Conflicts: glibc <= 2.0.7" to prevent installing guile in proper
  enviroment,
- simplifications in %files,
- Group in devel and static changed to Development/Libraries.

* Sun Dec 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3-2d]
- major changes -- for PLD. 

* Wed Dec  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-2]
- added using LDFLAGS="-s" to ./configure enviroment,
- added guile-libtool.patch for correct linking shared libraries.

* Sun Nov  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-1]
- added %clean section.

* Tue Sep  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-6]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files,
- added stripping shared libraries,
- all %doc moved to devel,
- simplification in %install and %files,
- changed permiddion on shared libraries to 755,
- %%{version} macro instead %%{PACKAGE_VERSION}.

* Wed Apr 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-5]
- added %clean section,
- Buildroot changed to /tmp/gile-%%{PACKAGE_VERSION}-root,
- replaced "mkdir -p" with "install -d" in %install,
- addec "Requires: guile = %{PACKAGE_VERSION}" for devel subpackage,
- added %defattr macros in %files (requires rpm >= 2.4.99).

* Thu Sep 18 1997 Tomasz K³oczko <kloczek@idk.com.pl>
  [1.2-3]
- added %attr(-, root, root) for %doc, 
- in %post, %postun ldconfig runed as parameter "-p",
- removed /bin/sh from requires,
- added %description,
- changes in %files.

* Fri Jul 11 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>  (1.2-2)
  [1.2-2]
- all rewrited for using Buildroot,
- added %postun,
- removed making buid logs,
- removed "--inclededir", added "--enable-dynamic-linking" to configure
  parameters,
- added stripping shared libs and /usr/bin/guile,
- added "Requires: /bin/sh" (for guile-snarf) in guile package and
  "Requires: m4" for guile-devel,
- added macro %%{PACKAGE_VERSION} in "Source:" and %files,
- added %attr macros in %files.
