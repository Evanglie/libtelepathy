Summary:	A GLib library to ease writing telepathy clients
Name:		libtelepathy
Version:	0.0.51
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/libtelepathy/%{name}-%{version}.tar.gz
# Source0-md5:	28a32062868f29b19f535476e422417b
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtelepathy is a D-Bus framework for unifying real time
communication, including instant messaging, voice calls and video
calls. It abstracts differences between protocols to provide a unified
interface for applications.

%package devel
Summary:	Header files for libtelepathy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtelepathy
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.61
Requires:	glib2-devel >= 2.4.0
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libtelepathy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtelepathy.

%package static
Summary:	Static libtelepathy library
Summary(pl.UTF-8):	Statyczna biblioteka libtelepathy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtelepathy library.

%description static -l pl.UTF-8
Statyczna biblioteka libtelepathy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libtelepathy.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy.so
%dir %{_includedir}/telepathy-1.0
%dir %{_includedir}/telepathy-1.0/libtelepathy
%{_includedir}/telepathy-1.0/libtelepathy/*.h
%{_libdir}/libtelepathy.la
%{_pkgconfigdir}/libtelepathy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy.a
