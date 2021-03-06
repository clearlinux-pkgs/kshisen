#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kshisen
Version  : 21.04.2
Release  : 28
URL      : https://download.kde.org/stable/release-service/21.04.2/src/kshisen-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/kshisen-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/kshisen-21.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kshisen-bin = %{version}-%{release}
Requires: kshisen-data = %{version}-%{release}
Requires: kshisen-license = %{version}-%{release}
Requires: kshisen-locales = %{version}-%{release}
Requires: kmahjongg
Requires: libkmahjongg
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : docbook2X
BuildRequires : extra-cmake-modules-data
BuildRequires : kmahjongg
BuildRequires : libkdegames-dev
BuildRequires : libkmahjongg
BuildRequires : libkmahjongg-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kshisen package.
Group: Binaries
Requires: kshisen-data = %{version}-%{release}
Requires: kshisen-license = %{version}-%{release}

%description bin
bin components for the kshisen package.


%package data
Summary: data components for the kshisen package.
Group: Data

%description data
data components for the kshisen package.


%package doc
Summary: doc components for the kshisen package.
Group: Documentation

%description doc
doc components for the kshisen package.


%package license
Summary: license components for the kshisen package.
Group: Default

%description license
license components for the kshisen package.


%package locales
Summary: locales components for the kshisen package.
Group: Default

%description locales
locales components for the kshisen package.


%prep
%setup -q -n kshisen-21.04.2
cd %{_builddir}/kshisen-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623399924
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623399924
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kshisen
cp %{_builddir}/kshisen-21.04.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kshisen/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kshisen-21.04.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kshisen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang kshisen

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kshisen

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kshisen.desktop
/usr/share/config.kcfg/kshisen.kcfg
/usr/share/icons/hicolor/128x128/apps/kshisen.png
/usr/share/icons/hicolor/16x16/apps/kshisen.png
/usr/share/icons/hicolor/22x22/apps/kshisen.png
/usr/share/icons/hicolor/32x32/apps/kshisen.png
/usr/share/icons/hicolor/48x48/apps/kshisen.png
/usr/share/icons/hicolor/64x64/apps/kshisen.png
/usr/share/metainfo/org.kde.kshisen.appdata.xml
/usr/share/qlogging-categories5/kshisen.categories
/usr/share/sounds/kshisen/tile-fall-tile.ogg
/usr/share/sounds/kshisen/tile-touch.ogg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/cs/kshisen/index.cache.bz2
/usr/share/doc/HTML/cs/kshisen/index.docbook
/usr/share/doc/HTML/de/kshisen/index.cache.bz2
/usr/share/doc/HTML/de/kshisen/index.docbook
/usr/share/doc/HTML/de/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/en/kshisen/gameboard.png
/usr/share/doc/HTML/en/kshisen/index.cache.bz2
/usr/share/doc/HTML/en/kshisen/index.docbook
/usr/share/doc/HTML/en/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/es/kshisen/index.cache.bz2
/usr/share/doc/HTML/es/kshisen/index.docbook
/usr/share/doc/HTML/et/kshisen/index.cache.bz2
/usr/share/doc/HTML/et/kshisen/index.docbook
/usr/share/doc/HTML/fr/kshisen/index.cache.bz2
/usr/share/doc/HTML/fr/kshisen/index.docbook
/usr/share/doc/HTML/fr/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/fr/kshisen/score-formula.png
/usr/share/doc/HTML/it/kshisen/index.cache.bz2
/usr/share/doc/HTML/it/kshisen/index.docbook
/usr/share/doc/HTML/ja/kshisen/index.cache.bz2
/usr/share/doc/HTML/ja/kshisen/index.docbook
/usr/share/doc/HTML/ja/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/nl/kshisen/index.cache.bz2
/usr/share/doc/HTML/nl/kshisen/index.docbook
/usr/share/doc/HTML/pl/kshisen/index.cache.bz2
/usr/share/doc/HTML/pl/kshisen/index.docbook
/usr/share/doc/HTML/pl/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/pt/kshisen/index.cache.bz2
/usr/share/doc/HTML/pt/kshisen/index.docbook
/usr/share/doc/HTML/pt_BR/kshisen/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kshisen/index.docbook
/usr/share/doc/HTML/ru/kshisen/index.cache.bz2
/usr/share/doc/HTML/ru/kshisen/index.docbook
/usr/share/doc/HTML/sv/kshisen/index.cache.bz2
/usr/share/doc/HTML/sv/kshisen/index.docbook
/usr/share/doc/HTML/sv/kshisen/kshisen-configuration.png
/usr/share/doc/HTML/uk/kshisen/gameboard.png
/usr/share/doc/HTML/uk/kshisen/index.cache.bz2
/usr/share/doc/HTML/uk/kshisen/index.docbook
/usr/share/doc/HTML/uk/kshisen/kshisen-configuration.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kshisen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kshisen/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f kshisen.lang
%defattr(-,root,root,-)

