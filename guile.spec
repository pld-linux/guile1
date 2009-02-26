#
# Conditional build:
%bcond_without	tests	# don't perform ./check-guile
%bcond_without	emacs	# don't build emacs subpackage
#
%define		ver	1.8
Summary:	GNU Extension language
Summary(es.UTF-8):	Lenguaje de extensión de la GNU
Summary(ja.UTF-8):	アプリケーションの拡張のための GNU による Scheme の実装
Summary(pl.UTF-8):	Język GNU Extension language
Summary(pt_BR.UTF-8):	Linguagem de extensão da GNU
Summary(ru.UTF-8):	Язык расширений GNU
Summary(uk.UTF-8):	Мова розширень GNU
Name:		guile
Version:	1.8.6
Release:	1
Epoch:		5
License:	GPL v2+/LGPL v2.1+
Group:		Development/Languages
Source0:	http://ftp.gnu.org/gnu/guile/%{name}-%{version}.tar.gz
# Source0-md5:	9e23d3dbea0e89bab8a9acc6880150de
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_awk_patch.patch
Patch2:		%{name}-unknown_arch.patch
Patch3:		%{name}-test-hacks.patch
Patch4:		%{name}-as-needed.patch
URL:		http://www.gnu.org/software/guile/guile.html
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
%{?with_emacs:BuildRequires:	emacs}
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
Requires:	umb-scheme
Obsoletes:	libguile9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch sparc sparc64
%undefine	with_tests
%endif

%description
Guile, a portable, embeddable Scheme implementation written in C.
Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%description -l es.UTF-8
Guile es una implementación de Scheme, que puede ser portátil y
empotrada, escrita en C. Guile provee una máquina de ejecución
independiente de plataforma, que puede ser linkada como una biblioteca
construyendo programas extensibles.

%description -l ja.UTF-8
GUILE (GNU's Ubiquitous Intelligent Language for Extension) は Scheme
プログラミング言語を実装した C で書かれたライブラリです。 GUILE は
マシン非依存の実行環境で、プログラムの拡張性を提供します。

%description -l pl.UTF-8
Guile jest przenośną, dającą się wbudować implementacją Scheme
napisaną w C. Guile udostępnia platformę wykonywania niezależną od
sprzętu, która może być dołączona jako biblioteka przy tworzeniu
rozszerzalnych programów.

%description -l pt_BR.UTF-8
Guile é um implementação de Scheme portável e embutível escrita em C.
Guile provê uma máquina de execução independente de plataforma, que
pode ser ligada como uma biblioteca construindo programas extensíveis.

%description -l ru.UTF-8
Guile - это переносимая, встраиваемая реализация языка Scheme
написанная на C. Guile предоставляет машинонезависимую среду
исполнения, которая может быть скомпонована с программой в виде
библиотеки.

%description -l uk.UTF-8
Guile - це переносима та вбудовувана реалізація мови Scheme написана
на C. Guile забезпечує машинонезалежне середовище виконання, яке може
бути скомпоноване з програмою у вигляді бібліотеки.

%package devel
Summary:	Guile's header files, etc
Summary(es.UTF-8):	Bibliotecas de Guile, archivos de inclusión, etc
Summary(ja.UTF-8):	GUILE 拡張性ライブラリ用のライブラリとヘッダファイル
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja Guile
Summary(pt_BR.UTF-8):	Bibliotecas da Guile, arquivos de inclusão, etc
Summary(ru.UTF-8):	Файлы для разработки программ с Guile
Summary(uk.UTF-8):	Файли для розробки програм з Guile
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gmp-devel >= 4.1
Requires:	libltdl-devel
Requires:	m4
Obsoletes:	libguile9-devel

%description devel
What's needed to develop apps linked w/ guile

%description devel -l es.UTF-8
Este paquete contiene todo lo necesario para desarrollar aplicaciones
usando Guile.

%description -l ja.UTF-8
guile-devel パッケージはライブラリやヘッダファイル、その他...あなたが
GUILE 拡張性ライブラリをリンクしたプログラムを作成するのに必要な
ファイルを提供します。

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja Guile.

%description devel -l pt_BR.UTF-8
Este pacote contém o que é necessário para desenvolver aplicações
usando a Guile.

%description devel -l ru.UTF-8
Все, что нужно для разработки приложений, скомпонованых с guile.

%description devel -l uk.UTF-8
Все, що потрібно для розробки програм, що компонуються з guile.

%package static
Summary:	Guile static libraries
Summary(pl.UTF-8):	Biblioteka statyczna Guile
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com guile
Summary(ru.UTF-8):	Статические библиотеки Guile
Summary(uk.UTF-8):	Статичні бібліотеки Guile
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Guile static library.

%description static -l pl.UTF-8
Biblioteka statyczna Guile.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com guile

%description static -l ru.UTF-8
Статические библиотеки guile.

%description static -l uk.UTF-8
Статичні бібліотеки guile.

%package -n emacs-guile-mode-pkg
Summary:	emacs guile-mode
Summary(pl.UTF-8):	Tryb guile dla emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs

%description -n emacs-guile-mode-pkg
Emacs guile-mode.

%description -n emacs-guile-mode-pkg -l pl.UTF-8
Tryb edycji guile dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd guile-readline
%{__libtoolize}
%{__aclocal} -I ../guile-config
%{__autoconf}
# DON'T USE --force HERE - it would break build
automake -a -c --foreign
cd ..
%configure \
	--enable-error-on-warning=no

%{__make}

%{?with_tests:%{__make} -C libguile stack-limit-calibration.scm}
%{?with_tests:./check-guile}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/guile/site,%{_libdir}/guile}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/guile
%attr(755,root,root) %{_bindir}/guile-tools
%attr(755,root,root) %{_libdir}/libguile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile.so.17
# shared libraries dlopened by interpreter (.so or .la needed)
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-1-v-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-srfi-srfi-1-v-3.so.3
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-1-v-3.so
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-4-v-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-srfi-srfi-4-v-3.so.3
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-4-v-3.so
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-13-14-v-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-srfi-srfi-13-14-v-3.so.3
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-13-14-v-3.so
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-60-v-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-srfi-srfi-60-v-2.so.2
%attr(755,root,root) %{_libdir}/libguile-srfi-srfi-60-v-2.so
%attr(755,root,root) %{_libdir}/libguilereadline-v-17.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguilereadline-v-17.so.17
%attr(755,root,root) %{_libdir}/libguilereadline-v-17.so
%{_libdir}/guile
%dir %{_datadir}/guile
%dir %{_datadir}/guile/%{ver}
%{_datadir}/guile/%{ver}/guile-procedures.txt
%{_datadir}/guile/%{ver}/ice-9
%{_datadir}/guile/%{ver}/lang
%{_datadir}/guile/%{ver}/oop
%dir %{_datadir}/guile/%{ver}/scripts
%attr(755,root,root) %{_datadir}/guile/%{ver}/scripts/*
%{_datadir}/guile/%{ver}/srfi
%dir %{_datadir}/guile/site
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING
%attr(755,root,root) %{_bindir}/guile-config
%attr(755,root,root) %{_bindir}/guile-snarf
%attr(755,root,root) %{_libdir}/libguile.so
%{_libdir}/libguile.la
%{_libdir}/libguile-srfi-srfi-1-v-3.la
%{_libdir}/libguile-srfi-srfi-4-v-3.la
%{_libdir}/libguile-srfi-srfi-13-14-v-3.la
%{_libdir}/libguile-srfi-srfi-60-v-2.la
%{_libdir}/libguilereadline-v-17.la
%{_infodir}/goops.info*
%{_infodir}/guile.info*
%{_infodir}/guile-tut.info*
%{_infodir}/r5rs.info*
%{_includedir}/guile
%{_includedir}/libguile
%{_includedir}/libguile.h
%{_pkgconfigdir}/guile-1.8.pc
%{_aclocaldir}/guile.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libguile.a
%{_libdir}/libguile-srfi-srfi-1-v-3.a
%{_libdir}/libguile-srfi-srfi-4-v-3.a
%{_libdir}/libguile-srfi-srfi-13-14-v-3.a
%{_libdir}/libguile-srfi-srfi-60-v-2.a
%{_libdir}/libguilereadline-v-17.a

%if %{with emacs}
%files -n emacs-guile-mode-pkg
%defattr(644,root,root,755)
%{_emacs_lispdir}/*.el
%endif
