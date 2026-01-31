%global debug_package %{nil}
%define uname SPECTRWM
%define uver 3_6_0

Name:		spectrwm
Version:	3.6.0
Release:	1
Source0:	https://github.com/conformal/spectrwm/archive/refs/tags/%{uname}_%{uver}.tar.gz
Summary:	spectrwm is a small, dynamic tiling and reparenting window manager for X11
URL:		https://github.com/conformal/spectrwm
License:	ISC
Group:		Graphical Desktop

BuildRequires:	make
BuildRequires:  lib64bsd-devel
BuildRequires:  lib64xcb-icccm4
BuildRequires:  lib64xcb-util-devel
BuildRequires:  lib64xcb-util-keysyms-devel
BuildRequires:  lib64xcb-util-wm-devel
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xft)

Requires:  fontconfig
Requires:  glibc
Requires:  lib64bsd0
Requires:  lib64x11-xcb1
Requires:  lib64xcursor1
Requires:  lib64xft2
Requires:  lib64xcb-util1
Requires:  lib64xcb-util-keysyms1

Recommends:     dmenu

%description
%{summary}.
%prep
%autosetup -p1 -n %{name}-%{uname}_%{uver}
#Change the Makefile to install files to /usr rather than /usr/local
sed 's|/usr/local|$(DESTDIR)$(PREFIX)|g' linux/Makefile

%build
cd linux
make PREFIX=%{_prefix}

%install
cd linux
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%files
%{_bindir}/scrotwm
%{_bindir}/%{name}
%{_prefix}/%{_sysconfdir}/%{name}.conf
%{_prefix}/lib/libswmhack*
%{_datadir}/xsessions/%{name}.desktop
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/LICENSE.md
%{_docdir}/%{name}/examples/*
%{_mandir}/man1/%{name}.1.zst
