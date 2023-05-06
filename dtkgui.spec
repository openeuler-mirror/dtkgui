Name:           dtkgui
Version:        5.5.18
Release:        1
Summary:        Deepin dtkgui
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkgui

%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}-%{version}.orig.tar.xz
%endif
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  dtkcore-devel
BuildRequires:  librsvg2-devel
BuildRequires:  gcc-c++
BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Dtkgui is the GUI module for DDE look and feel.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} \
           DTK_VERSION=%{version} \
           LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk5 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/dtk5/deepin-gui-settings
%{_libexecdir}/dtk5/taskbar
%{_libexecdir}/dtk5/dde-kwin-debug

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/dtkgui.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkgui.pri
%{_libdir}/cmake/DtkGui/
%{_libdir}/lib%{name}.so

%changelog
* Thu Mar 23 2023 liweiganga <liweiganga@uniontech.com> - 5.5.18-1
- update to 5.5.18

* Tue Jul 19 2022 konglidong <konglidong@uniontech.com> - 5.4.10-1
- Update to 5.4.10

* Sat Jan 29 2022 liweigang <liweiganga@uniontech.com> - 5.2.2.1-3
- fix build error

* Thu Jul 15 2021 weidong <weidong@uniontech.com> - 5.2.2.1-2
- Format spec

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.2.2.1-1
- Update 5.2.2.1

* Thu Sep 3 2020 weidong <weidong@uniontech.com> - 5.2.0-2
- fix source url in spec

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-1
- Package init
