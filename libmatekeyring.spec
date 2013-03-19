#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Framework for managing passwords and other secrets
Name:		libmatekeyring
Version:	1.5.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	846f5370e793f519bd5f68ab912eb3a5
URL:		http://wiki.mate-desktop.org/libmatekeyring
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 2.16.0
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgcrypt-devel
BuildRequires:	mate-common
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmatekeyring is a program that keep password and other secrets for
users. The library libmatekeyring is used by applications to integrate
with the libmatekeyring system.

%package devel
Summary:	Development files for libmate-keyring
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

%description devel
The libmatekeyring-devel package contains the libraries and header
files needed to develop applications that use libmate-keyring.

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
NOCONFIGURE=1 ./autogen.sh
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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libmate-keyring.so.*.*.*
%ghost %{_libdir}/libmate-keyring.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmate-keyring.so
%{_pkgconfigdir}/mate-keyring-1.pc
%{_includedir}/mate-keyring-1

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mate-keyring
