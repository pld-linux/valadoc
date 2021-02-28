# NOTE: for versions >= 0.38 see vala.spec
Summary:	Documentation tool for Vala
Summary(pl.UTF-8):	Narzędzie obsługujące dokumentację dla języka Vala
Name:		valadoc
Version:	0.36.2
Release:	0.1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/valadoc/0.36/%{name}-%{version}.tar.xz
# Source0-md5:	cd62baa5d6d3321e1f86e43ef596be98
URL:		https://wiki.gnome.org/Projects/Valadoc
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	graphviz-devel >= 2.16
BuildRequires:	help2man
BuildRequires:	libgee-devel >= 0.20.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.36
BuildRequires:	vala-libgee >= 0.20
BuildRequires:	xz
Requires:	glib2 >= 1:2.24.0
Requires:	graphviz >= 2.16
Requires:	libgee >= 0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Documentation tool for Vala.

%description -l pl.UTF-8
Narzędzie obsługujące dokumentację dla języka Vala.

%package devel
Summary:	Header file for Valadoc library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Valadoc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.24.0
Requires:	graphviz-devel >= 2.16
Requires:	libgee-devel >= 0.20

%description devel
Header file for Valadoc library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki Valadoc.

%package -n vala-valadoc
Summary:	Vala API for Valadoc library
Summary(pl.UTF-8):	API języka Vala do biblioteki Valadoc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.26
Requires:	vala-libgee >= 0.20
BuildArch:	noarch

%description -n vala-valadoc
Vala API for Valadoc library.

%description -n vala-valadoc -l pl.UTF-8
API języka Vala do biblioteki Valadoc.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/valadoc/*/*/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvaladoc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS
%attr(755,root,root) %{_bindir}/valadoc
%attr(755,root,root) %{_libdir}/libvaladoc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvaladoc.so.0
%dir %{_libdir}/valadoc
%dir %{_libdir}/valadoc/doclets
%dir %{_libdir}/valadoc/doclets/devhelp
%attr(755,root,root) %{_libdir}/valadoc/doclets/devhelp/libdoclet.so
%dir %{_libdir}/valadoc/doclets/gtkdoc
%attr(755,root,root) %{_libdir}/valadoc/doclets/gtkdoc/libdoclet.so
%dir %{_libdir}/valadoc/doclets/html
%attr(755,root,root) %{_libdir}/valadoc/doclets/html/libdoclet.so
%dir %{_libdir}/valadoc/drivers
%dir %{_libdir}/valadoc/drivers/0.36.x
%attr(755,root,root) %{_libdir}/valadoc/drivers/0.36.x/libdriver.so
%{_datadir}/valadoc
%{_mandir}/man1/valadoc.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvaladoc.so
%{_includedir}/valadoc-1.0.h
%{_pkgconfigdir}/valadoc-1.0.pc

%files -n vala-valadoc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/valadoc-1.0.deps
%{_datadir}/vala/vapi/valadoc-1.0.vapi
