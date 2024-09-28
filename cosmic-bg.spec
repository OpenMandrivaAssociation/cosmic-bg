%undefine _debugsource_packages
%define         appname com.system76.CosmicBackground
Name:           cosmic-bg
Version:        1.0.0
Release:        0.alpha2.0
Summary:        COSMIC service for backgrounds
Group:          Desktop/COSMIC
License:        MPL-2.0
URL:            https://github.com/pop-os/cosmic-bg
Source0:        https://github.com/pop-os/cosmic-applibrary/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  mold
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
COSMIC session service which applies backgrounds to displays.
Supports the following features:

    Supports common image formats supported by image-rs
    8 and 10-bit background surface layers
    Use of colors and gradients for backgrounds
    Per-display background application
    Wallpaper slideshows that alternate between backgrounds periodically

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.2 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/cosmic
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
