Summary:	GNU Extension language
Summary(pl):	GNU Extension language
Name:		guile
Version:	1.4
Release:	12
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://prep.ai.mit.edu/pub/gnu/guile/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.pach
Patch1:		%{name}-fix_awk_patch.patch
Patch2:		%{name}-std_headers.patch
Patch3:		%{name}-SCM_SITE_DIR_path.patch
Patch4:		%{name}-acinclude.m4_fixes.patch
Patch5:		%{name}-am_fixes.patch
Patch6:		%{name}-use_system_libltd.aptch
BuildRequires:	libltdl-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
Requires:	umb-scheme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libguile9

%description
Guile, a portable, embeddable Scheme implementation written in C.
Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%description -l pl
Guile jest implementacj± Scheme napisan± w C.

%package devel
Summary:	Guile's header files, etc
Summary(pl):	Pliki nag³ówkowe i dokumentacja Guile
Group:		Development/Libraries
Requires:	m4
Requires:	%{name} = %{version}
Requires:	ncurses-devel >= 5.2
Requires:	readline-devel >= 4.2
Obsoletes:	libguile9-devel

%description devel
What's needed to develop apps linked w/ guile

%description devel -l pl
Pliki nag³ówkowe i dokumentacja Guile.

%package static
Summary:	Guile static libraries
Summary(pl):	Biblioteka statyczna Guile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Guile static library.

%description static -l pl
Biblioteka statyczna Guile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
#rm -f missing
#libtoolize --copy --force
#aclocal -I .
#autoconf
#automake -a -c -f
#(cd guile-readline
#aclocal
#autoconf
#automake -a -c -f)
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/guile/site,%{_libdir}/guile}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog GUILE-VERSION HACKING NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/guile
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_libdir}/guile
%{_datadir}/guile

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,GUILE-VERSION,HACKING,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/guile-config
%attr(755,root,root) %{_bindir}/guile-doc-snarf
%attr(755,root,root) %{_bindir}/guile-snarf*
%attr(755,root,root) %{_bindir}/guile-func-name-check
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_infodir}/*info*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
