Name:		kapman
Version:	15.04.2
Release:	1
Epoch:		1
Summary:	A Pac-Man clone
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kapman/
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)

%description
Kapman is a clone of the well known game Pac-Man.

You must run through the maze to eat all pills without being captured by a
ghost. By eating an energizer, Kapman gets the ability to eat ghosts for a few
seconds. When a stage is cleared of pills and energizer the player is taken to
the next stage with slightly increased game speed.

%files
%{_kde_bindir}/kapman
%{_kde_applicationsdir}/kapman.desktop
%{_kde_appsdir}/kapman
%{_kde_docdir}/*/*/kapman
%{_kde_iconsdir}/hicolor/*/apps/kapman.*
%{_kde_datadir}/sounds/kapman

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
