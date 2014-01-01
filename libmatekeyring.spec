#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Framework for managing passwords and other secrets
Summary(pl.UTF-8):	Szkielet do zarządzania hasłami i innymi tajnymi danymi
Name:		libmatekeyring
Version:	1.6.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	2c20a62778f4bf8240011fe03c97a05e
URL:		http://wiki.mate-desktop.org/libmatekeyring
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgcrypt-devel >= 1.2.2
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus-libs >= 1.0
Requires:	glib2 >= 1:2.16.0
Requires:	libgcrypt >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-keyring is a program that keep password and other secrets for
users. The library libmate-keyring is used by applications to
integrate with the MATE keyring system. libmatekeyring is a fork of
libgnomekeyring.

%description -l pl.UTF-8
mate-keyring to program przechowujący hasła oraz inne tajne dane
użytkowników. Biblioteka libmate-keyring jest używana przez aplikacje
do integracji z systemem kluczy MATE. libmatekeyring to odgałęzienie
libgnomekeyring.

%package devel
Summary:	Development files for libmate-keyring
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libmate-keyring
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0

%description devel
The libmatekeyring-devel package contains the header files needed to
develop applications that use libmate-keyring.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne przy tworzeniu aplikacji
wykorzystujących bibliotekę libmate-keyring.

%package apidocs
Summary:	libmate-keyring library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmate-keyring
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmate-keyring library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmate-keyring.

%prep
%setup -q

%build
%{__intltoolize}
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmate-keyring.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmate-keyring.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmate-keyring.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmate-keyring.so
%{_includedir}/mate-keyring-1
%{_pkgconfigdir}/mate-keyring-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mate-keyring
