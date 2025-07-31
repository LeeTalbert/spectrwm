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

Recommends:     dmenu

%description
spectrwm is a small, dynamic tiling and reparenting window manager for X11. It tries to stay out of the way so that valuable screen real estate can be used for much more important stuff. It has sane defaults, and it does not require one to learn a language to do any configuration. spectrwm is written by hackers for hackers, and it strives to be small, compact, and fast.

spectrwm was largely inspired by xmonad and dwm. Both are fine products, but they suffer from things like: crazy-unportable-language syndrome, silly defaults, asymmetrical window layout, the 'how hard can it be?' (to code efficiently) problem, and good old NIH. Nevertheless, dwm was a phenomenal resource, and good ideas and code were borrowed from it. On the other hand, xmonad has great defaults and key bindings, plus xinerama support, but it is crippled by not being written in C.

spectrwm is a beautiful pearl! For it, too, was created by grinding irritation. Nothing is a bigger waste of time either than moving windows around until they are the right size-ish or having just about any relevant key combination be eaten by some task one never performs. The path of agony is too long to quote, and, in classic OpenBSD fashion (put up, or hack up), a brand new window manager was whooped up to serve no other purpose than to obey its masters.

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
