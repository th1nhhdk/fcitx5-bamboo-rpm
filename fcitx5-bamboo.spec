Name:           fcitx5-bamboo
Version:        1.0.4
Release:        1%{?dist}
Summary:        Bamboo (Vietnamese Input Method) engine support for Fcitx

License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-bamboo
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-bamboo/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  golang
BuildRequires:  gcc-g++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSES/*
%doc README
%config %{_datarootdir}/fcitx5/addon/bamboo.conf
%config %{_datarootdir}/fcitx5/inputmethod/bamboo.conf
%{_prefix}/lib/debug/usr/lib64/fcitx5/*
%{_libdir}/fcitx5/*
%{_datarootdir}/fcitx5/bamboo/*
%{_datarootdir}/icons/hicolor/scalable/apps/*
%{_datarootdir}/locale/*
%{_metainfodir}/*


%changelog
* Mon Jul 24 2023 th1nhhdk <th1nhhdk@tutanota.com>
- Initial release.
