Summary:	A configuration reading and writing library
Summary(pl):	Biblioteka do odczytu i zapisu konfiguracji
Name:		keeper
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.inf.bme.hu/~mszeredi/keeper/%{name}-%{version}.tar.gz
# Source0-md5:	e5c142618aeee2eb0da8e1599d73de7d
Patch0:		%{name}-shared.patch
URL:		http://www.inf.bme.hu/~mszeredi/keeper/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The keeper library gives an extremely simple interface for reading and
writing configuration data. Data is stored in multiple text files, in
a hierarchical system. This package also contains a command-line tool
for examining and modifying the keeper database.

%description -l pl
Biblioteka keeper udostêpnia bardzo prosty interfejs do odczutu i
zapisu danych konfiguracyjnych. Dane s± zapisywane w wielu plikach
tekstowych w systemie hierarchicznym. Ten pakiet zawiera tak¿e
dzia³aj±ce z linii poleceñ narzêdzie do sprawdzania i modyfikowania
bazy danych keepera.

%package devel
Summary:	Header files for keeper library
Summary(pl):	Pliki nag³ówkowe biblioteki keeper
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for keeper library.

%description devel -l pl
Pliki nag³ówkowe biblioteki keeper.

%package static
Summary:	Static keeper library
Summary(pl):	Statyczna biblioteka keeper
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static keeper library.

%description static -l pl
Statyczna biblioteka keeper.

%package -n gkeeper
Summary:	A graphical tool for viewing and manipulating the keeper database
Summary(pl):	Graficzne narzêdzie do ogl±dania i modyfikowania bazy danych keepera
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description -n gkeeper
Gkeeper is a GTK+ based front-end for the keeper database. Gkeeper lets
you view, edit, create or delete entries in the database. The source
of gkeeper contains a good example, on how to store and retrieve the
menu accelerators using the keeper interface.

%description -n gkeeper -l pl
Gkeeper to oparty na GTK+ graficzny interfejs do bazy danych keeper.
Gkeeper pozwala na przegl±danie, edycjê, tworzenie i usuwanie wpisów w
bazie. ¬ród³a gkeepera zawieraj± dobry przyk³ad, jak zapisywaæ i
odtwarzaæ skróty klawiszowe menu przy u¿yciu interfejsu keepera.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_root="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/kptool
%attr(755,root,root) %{_libdir}/libkeeper.so.*.*.*
%{_mandir}/man1/kptool.1*

%files devel
%defattr(644,root,root,755)
%doc example/example.c
%attr(755,root,root) %{_libdir}/libkeeper.so
%{_libdir}/libkeeper.la
%{_includedir}/keeper.h
%{_mandir}/man3/keeper.3*
%{_mandir}/man3/kp_base.3*
%{_mandir}/man3/kp_utils.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libkeeper.a

%files -n gkeeper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gkeeper
