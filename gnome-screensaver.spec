#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-screensaver
Version  : 3.6.1
Release  : 11
URL      : https://download.gnome.org/sources/gnome-screensaver/3.6/gnome-screensaver-3.6.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-screensaver/3.6/gnome-screensaver-3.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libgnomekbdui)
BuildRequires : pkgconfig(libxklavier)
BuildRequires : pkgconfig(x11)
BuildRequires : systemd-dev
Patch1: 0001-data-Integrate-with-the-Clear-Linux-PAM-configuratio.patch
Patch2: gnome-desktop-3.36.patch

%description
gnome-screensaver
=================
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

%prep
%setup -q -n gnome-screensaver-3.6.1
cd %{_builddir}/gnome-screensaver-3.6.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661290889
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-pam-prefix=/usr/share
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1661290889
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-screensaver
cp %{_builddir}/gnome-screensaver-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-screensaver/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/gnome-screensaver-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-screensaver/d4e89d1a1e7812dae053aa8cb891f452891df932
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/autostart
cp src/gnome-screensaver.desktop %{buildroot}/usr/share/xdg/autostart/
## install_append end

%files
%defattr(-,root,root,-)
