%define PKGRELEASE 3.6

Summary:	The Persistence of Vision Raytracer
Name:		povray
Version:	3.6.1
Release:	%mkrel 4
Group:		Sciences/Computer science
License:	GPL
URL:		http://www.povray.org
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}.bash-completion.bz2
Patch0:		povray-3.6.1-config-0.2.0.diff.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	zlib1-devel
BuildRequires:	libpng-devel
BuildRequires:	X11-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel

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
%setup -q 
%patch0 -p1
bzcat %{SOURCE1} > %{name}.bash-completion

%build
%configure2_5x --with-x COMPILED_BY="Mandriva_Linux" --disable-optimiz
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.conf
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.ini
%doc doc/* 
%doc %{_mandir}/man1/povray.*
%{_bindir}/povray
%{_defaultdocdir}/%{name}-%PKGRELEASE
%{_datadir}/%{name}-%PKGRELEASE
