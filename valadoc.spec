Summary:	Documentation tool for Vala
Summary(pl.UTF-8):	Narzędzie obsługujące dokumentację dla języka Vala
Name:		valadoc
Version:	0.3.2
%define	snap	20120223
Release:	0.%{snap}.1
License:	LGPL v2.1+
Group:		Development/Tools
# git clone git://git.gnome.org/valadoc
Source0:	%{name}.tar.xz
# Source0-md5:	c628fb81342eed958c6bdc63966528a2
URL:		https://live.gnome.org/Valadoc
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	graphviz-devel >= 2.16
BuildRequires:	libgee0.6-devel >= 0.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.18
BuildRequires:	vala-libgee0.6 >= 0.5
BuildRequires:	xz
Requires:	glib2 >= 1:2.12.0
Requires:	graphviz >= 2.16
Requires:	libgee0.6 >= 0.5
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
Requires:	glib2-devel >= 1:2.12.0
Requires:	graphviz-devel >= 2.16
Requires:	libgee0.6-devel >= 0.5

%description devel
Header file for Valadoc library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki Valadoc.

%package -n vala-valadoc
Summary:	Vala API for Valadoc library
Summary(pl.UTF-8):	API języka Vala do biblioteki Valadoc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18
Requires:	vala-libgee0.6 >= 0.5

%description -n vala-valadoc
Vala API for Valadoc library.

%description -n vala-valadoc -l pl.UTF-8
API języka Vala do biblioteki Valadoc.

%prep
%setup -q -n %{name}

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
%doc AUTHORS MAINTAINERS THANKS
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
%dir %{_libdir}/valadoc/drivers/0.18.x
%attr(755,root,root) %{_libdir}/valadoc/drivers/0.18.x/libdriver.so
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
