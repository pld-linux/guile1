Summary:	GNU Extension language
Summary(es):	Lenguaje de extensión de la GNU
Summary(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤Î³ÈÄ¥¤Î¤¿¤á¤Î GNU ¤Ë¤è¤ë Scheme ¤Î¼ÂÁõ
Summary(pl):	GNU Extension language
Summary(pt_BR):	Linguagem de extensão da GNU
Summary(ru):	ñÚÙË ÒÁÓÛÉÒÅÎÉÊ GNU
Summary(uk):	íÏ×Á ÒÏÚÛÉÒÅÎØ GNU
Name:		guile
Version:	1.4.1
Release:	5
Epoch:		5
License:	GPL
Group:		Development/Languages
Source0:	ftp://prep.ai.mit.edu/pub/gnu/guile/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/guile/guile.html
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_awk_patch.patch
Patch2:		%{name}-SCM_SITE_DIR_path.patch
Patch3:		%{name}-sizet.patch
Patch4:		%{name}-axp.patch
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

%description -l es
Guile es una implementación de Scheme, que puede ser portátil y
empotrada, escrita en C. Guile provee una máquina de ejecución
independiente de plataforma, que puede ser linkada como una biblioteca
construyendo programas extensibles.

%description -l ja
GUILE (GNU's Ubiquitous Intelligent Language for Extension) ¤Ï Scheme
¥×¥í¥°¥é¥ß¥ó¥°¸À¸ì¤ò¼ÂÁõ¤·¤¿ C ¤Ç½ñ¤«¤ì¤¿¥é¥¤¥Ö¥é¥ê¤Ç¤¹¡£ GUILE ¤Ï
¥Þ¥·¥óÈó°ÍÂ¸¤Î¼Â¹Ô´Ä¶­¤Ç¡¢¥×¥í¥°¥é¥à¤Î³ÈÄ¥À­¤òÄó¶¡¤·¤Þ¤¹¡£

%description -l pl
Guile jest implementacj± Scheme napisan± w C.

%description -l pt_BR
Guile é um implementação de Scheme portável e embutível escrita em C.
Guile provê uma máquina de execução independente de plataforma, que
pode ser ligada como uma biblioteca construindo programas extensíveis.

%description -l ru
Guile - ÜÔÏ ÐÅÒÅÎÏÓÉÍÁÑ, ×ÓÔÒÁÉ×ÁÅÍÁÑ ÒÅÁÌÉÚÁÃÉÑ ÑÚÙËÁ Scheme
ÎÁÐÉÓÁÎÎÁÑ ÎÁ C. Guile ÐÒÅÄÏÓÔÁ×ÌÑÅÔ ÍÁÛÉÎÏÎÅÚÁ×ÉÓÉÍÕÀ ÓÒÅÄÕ
ÉÓÐÏÌÎÅÎÉÑ, ËÏÔÏÒÁÑ ÍÏÖÅÔ ÂÙÔØ ÓËÏÍÐÏÎÏ×ÁÎÁ Ó ÐÒÏÇÒÁÍÍÏÊ × ×ÉÄÅ
ÂÉÂÌÉÏÔÅËÉ.

%description -l uk
Guile - ÃÅ ÐÅÒÅÎÏÓÉÍÁ ÔÁ ×ÂÕÄÏ×Õ×ÁÎÁ ÒÅÁÌ¦ÚÁÃ¦Ñ ÍÏ×É Scheme ÎÁÐÉÓÁÎÁ
ÎÁ C. Guile ÚÁÂÅÚÐÅÞÕ¤ ÍÁÛÉÎÏÎÅÚÁÌÅÖÎÅ ÓÅÒÅÄÏ×ÉÝÅ ×ÉËÏÎÁÎÎÑ, ÑËÅ ÍÏÖÅ
ÂÕÔÉ ÓËÏÍÐÏÎÏ×ÁÎÅ Ú ÐÒÏÇÒÁÍÏÀ Õ ×ÉÇÌÑÄ¦ Â¦ÂÌ¦ÏÔÅËÉ.

%package devel
Summary:	Guile's header files, etc
Summary(es):	Bibliotecas de Guile, archivos de inclusión, etc
Summary(ja):	GUILE ³ÈÄ¥À­¥é¥¤¥Ö¥é¥êÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤È¥Ø¥Ã¥À¥Õ¥¡¥¤¥ë
Summary(pl):	Pliki nag³ówkowe i dokumentacja Guile
Summary(pt_BR):	Bibliotecas da Guile, arquivos de inclusão, etc
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó Guile
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú Guile
Group:		Development/Libraries
Requires:	m4
Requires:	%{name} = %{version}
Requires:	ncurses-devel >= 5.2
Requires:	readline-devel >= 4.2
Obsoletes:	libguile9-devel

%description devel
What's needed to develop apps linked w/ guile

%description devel -l es
Este paquete contiene todo lo necesario para desarrollar aplicaciones
usando Guile.

%description -l ja
guile-devel ¥Ñ¥Ã¥±¡¼¥¸¤Ï¥é¥¤¥Ö¥é¥ê¤ä¥Ø¥Ã¥À¥Õ¥¡¥¤¥ë¡¢¤½¤ÎÂ¾...¤¢¤Ê¤¿¤¬
GUILE ³ÈÄ¥À­¥é¥¤¥Ö¥é¥ê¤ò¥ê¥ó¥¯¤·¤¿¥×¥í¥°¥é¥à¤òºîÀ®¤¹¤ë¤Î¤ËÉ¬Í×¤Ê
¥Õ¥¡¥¤¥ë¤òÄó¶¡¤·¤Þ¤¹¡£

%description devel -l pl
Pliki nag³ówkowe i dokumentacja Guile.

%description devel -l pt_BR
Este pacote contém o que é necessário para desenvolver aplicações
usando a Guile.

%description devel -l ru
÷ÓÅ, ÞÔÏ ÎÕÖÎÏ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ, ÓËÏÍÐÏÎÏ×ÁÎÙÈ Ó guile.

%description devel -l uk
÷ÓÅ, ÝÏ ÐÏÔÒ¦ÂÎÏ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ËÏÍÐÏÎÕÀÔØÓÑ Ú guile.

%package static
Summary:	Guile static libraries
Summary(pl):	Biblioteka statyczna Guile
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com guile
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ Guile
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ Guile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Guile static library.

%description static -l pl
Biblioteka statyczna Guile.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com guile

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ guile.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ guile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# I wouldn't apply it, it breaks other programs, but I have fixed it, so
# if you convince me... (but remember about perl, python, tcl and ruby ) (filon)
#%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
#rm -f missing
#libtoolize --copy --force
#aclocal -I guile-config
#autoconf
#automake -a -c -f
#cd guile-readline
#libtoolize --copy --force
#aclocal
#autoconf
#automake -a -c -f
#cd -
%configure \
	--with-threads

%{__make}
#	THREAD_LIBS_LOCAL=`pwd`/qt/.libs/libqthreads.so

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
%{__cc} -shared readline.lo -Wl,--rpath -Wl,%{_libdir} ../libguile/.libs/libguile.so \
-L%{_libdir} -lreadline -lncurses -Wl,-soname -Wl,libguilereadline.so.0 \
-o $RPM_BUILD_ROOT%{_libdir}/libguilereadline.so.0.0.1
cd -

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
%doc AUTHORS ChangeLog GUILE-VERSION HACKING NEWS README
%attr(755,root,root) %{_bindir}/guile-config
%attr(755,root,root) %{_bindir}/guile-snarf
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_infodir}/*info*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
