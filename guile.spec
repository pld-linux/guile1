Summary:	GNU Extension language
Summary(pl):	GNU Extension language
Name:		guile
Version:	1.3
Release:	7
Copyright:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		ftp://prep.ai.mit.edu/pub/gnu/guile/%{name}-%{version}.tar.gz
Patch0:		guile-libtool.patch
Patch1:		guile-ansi.patch
Patch2:		guile-scm.patch
Patch3:		guile-info.pach
Prereq:		/sbin/install-info
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
%configure %{_target} \
	--prefix=/usr \
	--enable-dynamic-linking
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/guile/site

make install prefix=$RPM_BUILD_ROOT/%{_prefix}

strip $RPM_BUILD_ROOT%{_libdir}/*.so.*.*

ln -s ../../lib/umb-scheme/slib $RPM_BUILD_ROOT%{_datadir}/guile/slib

gzip -9fn $RPM_BUILD_ROOT%{_infodir}/data-rep* \
	AUTHORS ChangeLog GUILE-VERSION HACKING NEWS README 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/data-rep.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/data-rep.info.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/guile

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,GUILE-VERSION,HACKING,NEWS,README}.gz
%{_infodir}/*info*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%changelog
* Fri May 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-7]
- spec writted by me,
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
