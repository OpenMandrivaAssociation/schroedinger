%define abi 1.0
%define major 0
%define libname %mklibname %name %abi %major
%define develname %mklibname -d %name

Name:           schroedinger
Version:        1.0.3
Release:        %mkrel 1
Summary:        Portable libraries for the high quality Dirac video codec

Group:          Video
License:        LGPL/MIT/MPL
URL:            http://schrodinger.sourceforge.net/
Source0:        http://diracvideo.schleef.org/download/schroedinger/schroedinger-%{version}.tar.gz
#Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-

BuildRequires:  liboil-devel >= 0.3.13
BuildRequires:  libgstreamer-plugins-base-devel >= 0.10
BuildRequires:  gtk-doc

%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package -n %libname
Group:          System/Libraries
Summary:        Portable libraries for the high quality Dirac video codec

%description -n %libname
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package -n %develname
Group:          Development/C
Summary:        Development files for schrodinger
Requires:       %{libname} = %{version}-%{release}
Provides: lib%name-devel = %{version}-%{release}

%description -n %develname
Development files for schrodinger

%package -n gstreamer0.10-schroedinger
Group:          Video
Summary:        GStreamer Plugins that implement Dirac video encoding and decoding

%description -n gstreamer0.10-schroedinger
GStreamer Plugins that implement Dirac video encoding and decoding

%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%{_libdir}/gstreamer-0.10/libgstschro.la

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig

%postun -n %libname  -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-%{abi}.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc

%files -n gstreamer0.10-schroedinger
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstschro.so

