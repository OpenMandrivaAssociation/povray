%define name	povray
%define version 3.6.1
%define PKGRELEASE 3.6
%define release %mkrel 2

Name:         	%{name}
License:      	povray
Version:        %{version}
Release:        %{release}
Group:        	Sciences/Computer science
Summary:      	Ray tracer
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}.bash-completion.bz2
URL:	      	http://www.povray.org
BuildRoot:      %{_tmppath}/%name-buildroot
BuildRequires:	zlib1-devel, libpng-devel, XFree86-devel, libjpeg-devel, libtiff-devel
Obsoletes:	povray-common, povray-official

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
rm -rf ${RPM_BUILD_ROOT}
%setup -q 
bzcat %{SOURCE1} > %{name}.bash-completion

%build
%configure --with-x COMPILED_BY="Mandriva_Linux"
%make 

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}
make install DESTDIR=$RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.conf
%config(noreplace) %{_sysconfdir}/%{name}/%PKGRELEASE/povray.ini
%doc doc/* 
%doc %{_mandir}/man1/povray.1.bz2
%{_defaultdocdir}/%{name}-%PKGRELEASE
%{_datadir}/%{name}-%PKGRELEASE

%{_bindir}/povray

%clean
rm -rf $RPM_BUILD_ROOT


