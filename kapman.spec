Name:		kapman
Version:	22.12.3
Release:	1
Epoch:		1
Summary:	A Pac-Man clone
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kapman/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDEGames)

%description
Kapman is a clone of the well known game Pac-Man.

You must run through the maze to eat all pills without being captured by a
ghost. By eating an energizer, Kapman gets the ability to eat ghosts for a few
seconds. When a stage is cleared of pills and energizer the player is taken to
the next stage with slightly increased game speed.

%files -f %{name}.lang
%{_bindir}/kapman
%{_datadir}/metainfo/org.kde.kapman.appdata.xml
%{_datadir}/applications/org.kde.kapman.desktop
%{_iconsdir}/hicolor/*/apps/kapman.png
%{_datadir}/kapman
%{_datadir}/sounds/kapman

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
