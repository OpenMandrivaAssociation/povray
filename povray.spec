%define debug_package	%{nil}
%define PKGRELEASE 3.7

Summary:	The Persistence of Vision Raytracer
Name:		povray
Version:	3.7.0
Release:	0.RC6.1
Group:		Sciences/Computer science
License:	GPL
URL:		https://www.povray.org
Source0:	http://www.povray.org/beta/source/povray-%{version}.RC6.tar.gz
Source1:	%{name}.bash-completion
Patch0:		povray-3.7.0-install.patch
Patch1:		povray-3.7.0-link.patch
Patch2:		povray-3.7.0-boost-time.patch
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	svgalib-devel
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	boost-devel

%description
The Persistence of Vision Ray tracer creates three-dimensional,
photo-realistic images using a rendering technique called ray tracing.
It reads in a text file containing information describing the objects and
lighting in a scene and generates an image of that scene from the view
point of a camera also described in the text file. Ray tracing is not
a fast process by any means, (the generation of a complex image can
take several hours) but it produces very high quality images
with realistic reflections, shading, perspective, and other effects.

%prep
%setup -qn povray-%{version}.RC6
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
autoreconf -fi
%configure2_5x --with-x COMPILED_BY="%_vendor" --disable-optimiz --with-boost-libdir=%{_libdir}
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%files 
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.conf
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.ini
%doc doc/* 
%doc %{_mandir}/man1/povray.*
%{_bindir}/povray
%{_defaultdocdir}/%{name}-%PKGRELEASE
%{_datadir}/%{name}-%PKGRELEASE
