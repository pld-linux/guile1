Summary:	GNU Extension language
Summary(pl):	GNU Extension language
Name:		guile
Version:	1.4.1
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://prep.ai.mit.edu/pub/gnu/guile/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/guile/guile.html
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_awk_patch.patch
Patch2:		%{name}-SCM_SITE_DIR_path.patch
BuildRequires:	libltdl-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
Requires:	umb-scheme
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.5
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

# I wouldn't apply it, it breaks other programs, but I have fixed it, so
# if you convince me... (but remember about perl, python, tcl and ruby ) (filon)
#%patch2 -p1

%build
rm -f missing
libtoolize -c -f
aclocal -I guile-config
autoconf
automake -a -c -f
cp ltmain.sh guile-readline
cd guile-readline
aclocal
autoconf
automake -a -c -f
cd -
%configure \
	--with-threads

%{__make} \
	THREAD_LIBS_LOCAL=`pwd`/qt/.libs/libqthreads.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/guile/site,%{_libdir}/guile}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

# this is a hack :-)
# libtool while installing links libguilereadline with installed libguile, so (in most
# cases) we get libguilereadline.so linked with (old) libguile.so.9 (!!!) and we cannot
# install it, so I had to fix it :-) (filon)
cd guile-readline
gcc -shared readline.lo -Wl,--rpath ../libguile/.libs/libguile.so -lreadline -lncurses -Wl,-soname -Wl,libguilereadline.so.0 \
-o $RPM_BUILD_ROOT%{_libdir}/libguilereadline.so.0.0.1
cd -

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
%attr(755,root,root) %{_bindir}/guile-snarf
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_infodir}/*info*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
