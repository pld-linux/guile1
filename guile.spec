Summary:     GNU Extension language
Name:        guile
Version:     1.3
Release:     1
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Copyright:   GPL
Group:       Development/Languages
Buildroot:   /tmp/%{name}-%{version}-root
Requires:    umb-scheme
Buildroot:	/tmp/%{name}-%{version}-root

Guile, a portable, embeddable Scheme implementation written in C.  Guile
Guile, a portable, embeddable Scheme implementation written in C. Guile
provides a machine independent execution platform that can be linked in as a
library when building extensible programs.
%package devel
Summary:     Guile's libraries, header files, etc.
Group:       Development/Languages
Requires:    m4, %{name} = %{version}

%description devel
What's needed to develop apps linked w/ guile

%package static
Summary:     Guile static libraries
Group:       Development/Languages
Requires:    %{name}-devel = %{version}

%description static
Guile static libraries.

%prep
%setup -q
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --enable-dynamic-linking

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/guile/site
make install prefix=$RPM_BUILD_ROOT/usr/
strip $RPM_BUILD_ROOT/usr/{lib/lib*.so.*.*,bin/guile}

ln -s ../../lib/umb-scheme/slib $RPM_BUILD_ROOT/usr/share/guile/slib

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/lib/lib*.so.*.*
/usr/share/guile

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog GUILE-VERSION HACKING NEWS README TODO
/usr/include/*.h
/usr/include/guile
/usr/include/libguile
/usr/lib/lib*so
%defattr(644,root,root,755)
%attr(644,root,root) /usr/lib/*.a
%attr(644, root, root) /usr/lib/lib*.a
* Mon Apr 19 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-5]
* Tue Sep  1 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
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

* Wed Apr 28 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-5]
- added %clean section,
- Buildroot changed to /tmp/gile-%%{PACKAGE_VERSION}-root,
- replaced "mkdir -p" with "install -d" in %install,
- addec "Requires: guile = %{PACKAGE_VERSION}" for devel subpackage,
- added %defattr macros in %files (requires rpm >= 2.4.99).

* Thu Sep 18 1997 Tomasz K這czko <kloczek@idk.com.pl>
  [1.2-3]
- added %attr(-, root, root) for %doc, 
- in %post, %postun ldconfig runed as parameter "-p",
* Mon Jan 26 1998 Marc Ewing <marc@redhat.com>
  [1.2-4]
- Started with spec from Tomasz Koczko <kloczek@idk.com.pl>
- added slib link

* Thu Sep 18 1997 Tomasz Koczko <kloczek@idk.com.pl>
- added %description,
- changes in %files.

* Fri Jul 11 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>  (1.2-2)
  [1.2-2]
- all rewrited for using Buildroot,
- added %postun,
* Fri Jul 11 1997 Tomasz Koczko <kloczek@rudy.mif.pg.gda.pl>  (1.2-2)
  [1.2-2]
  parameters,
- added stripping shared libs and /usr/bin/guile,
- added "Requires: /bin/sh" (for guile-snarf) in guile package and
  "Requires: m4" for guile-devel,
- added macro %%{PACKAGE_VERSION} in "Source:" and %files,
- added %attr macros in %files.
