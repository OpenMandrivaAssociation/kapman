#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-kapman
Version:	24.05.0
Release:	%{?git:0.%{git}.}1
Summary:	A Pac-Man clone
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kapman/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kapman/-/archive/%{gitbranch}/kapman-%{gitbranchd}.tar.bz2#/kapman-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kapman-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KDEGames6)

%description
Kapman is a clone of the well known game Pac-Man.

You must run through the maze to eat all pills without being captured by a
ghost. By eating an energizer, Kapman gets the ability to eat ghosts for a few
seconds. When a stage is cleared of pills and energizer the player is taken to
the next stage with slightly increased game speed.

%files -f kapman.lang
%{_bindir}/kapman
%{_datadir}/metainfo/org.kde.kapman.appdata.xml
%{_datadir}/applications/org.kde.kapman.desktop
%{_iconsdir}/hicolor/*/apps/kapman.png
%{_datadir}/kapman
%{_datadir}/sounds/kapman

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kapman-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kapman --with-html
