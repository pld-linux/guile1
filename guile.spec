# TODO: kill LDFLAGS (--as-needed) from `guile-config link` output
#
# Conditional build:
%bcond_without	tests	# don't perform ./check-guile
#
Summary:	GNU Extension language
Summary(es.UTF-8):	Lenguaje de extensión de la GNU
Summary(ja.UTF-8):	アプリケーションの拡張のための GNU による Scheme の実装
Summary(pl.UTF-8):	Język GNU Extension language
Summary(pt_BR.UTF-8):	Linguagem de extensão da GNU
Summary(ru.UTF-8):	Язык расширений GNU
Summary(uk.UTF-8):	Мова розширень GNU
Name:		guile
Version:	1.8.1
Release:	2
Epoch:		5
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/gnu/guile/%{name}-%{version}.tar.gz
# Source0-md5:	be792074780d597208a8cdfed976f559
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_awk_patch.patch
Patch2:		%{name}-SCM_SITE_DIR_path.patch
Patch3:		%{name}-unknown_arch.patch
Patch4:		%{name}-test-hacks.patch
Patch5:		%{name}-as-needed.patch
URL:		http://www.gnu.org/software/guile/guile.html
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
Requires:	umb-scheme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libguile9

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# I wouldn't apply it, it breaks other programs, but I have fixed it, so
# if you convince me... (but remember about perl, python, tcl and ruby ) (filon)
# patch2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I guile-config
%{__autoconf}
%{__automake}
cd guile-readline
%{__aclocal} -I ../guile-config
%{__autoconf}
# DON'T USE --force HERE - it would break build
automake -a -c --foreign
cd ..
%configure

%{__make}

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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/guile
%attr(755,root,root) %{_bindir}/guile-tools
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/guile
%{_datadir}/guile

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING
%attr(755,root,root) %{_bindir}/guile-config
%attr(755,root,root) %{_bindir}/guile-snarf
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_infodir}/*.info*
%{_includedir}/*guile*
%{_aclocaldir}/guile.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
