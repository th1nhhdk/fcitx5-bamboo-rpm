Name:           fcitx5-bamboo
Version:        1.0.4
Release:        2%{?dist}
Summary:        Bamboo (Vietnamese Input Method) engine support for Fcitx

License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-bamboo
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-bamboo/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  golang
BuildRequires:  gettext

%if 0%{?is_opensuse}
BuildRequires:  gcc-c++
BuildRequires:  appstream-glib
%else
BuildRequires:  gcc-g++
BuildRequires:  libappstream-glib
%endif

Requires:       fcitx5

%description
This package provides a Bamboo (Vietnamese Input Method) engine for Fcitx5, based on https://github.com/BambooEngine/bamboo-core.

%prep
%autosetup


%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build


%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_datarootdir}/metainfo/*.metainfo.xml


%files
%license LICENSES/*
%doc README
%config %{_datarootdir}/fcitx5/addon/bamboo.conf
%config %{_datarootdir}/fcitx5/inputmethod/bamboo.conf

%{_libdir}/fcitx5/*
%{_datarootdir}/fcitx5/bamboo/*
%{_datarootdir}/icons/hicolor/scalable/apps/*
%{_datarootdir}/locale/*
%{_datarootdir}/metainfo/*


%changelog
* Sat Sep 02 2023 th1nhhdk <th1nhhdk@tutanota.com>
- Added openSUSE support.
- Debuginfo is moved to a separate package.

* Mon Jul 24 2023 th1nhhdk <th1nhhdk@tutanota.com>
- Initial release.
