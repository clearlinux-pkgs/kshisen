#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kshisen
Version  : 23.08.5
Release  : 61
URL      : https://download.kde.org/stable/release-service/23.08.5/src/kshisen-23.08.5.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.5/src/kshisen-23.08.5.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.5/src/kshisen-23.08.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
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
BuildRequires : libkdegames-dev
BuildRequires : libkmahjongg-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kshisen-23.08.5
cd %{_builddir}/kshisen-23.08.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708384000
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708384000
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kshisen
cp %{_builddir}/kshisen-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kshisen/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kshisen-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kshisen/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kshisen-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kshisen/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kshisen-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kshisen/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kshisen-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kshisen/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kshisen
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kshisen
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
/usr/share/doc/HTML/ca/kshisen/gameboard.png
/usr/share/doc/HTML/ca/kshisen/index.cache.bz2
/usr/share/doc/HTML/ca/kshisen/index.docbook
/usr/share/doc/HTML/ca/kshisen/kshisen-configuration.png
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
/usr/share/package-licenses/kshisen/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kshisen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kshisen/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kshisen/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kshisen/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kshisen.lang
%defattr(-,root,root,-)

