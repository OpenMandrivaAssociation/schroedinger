%define abi 1.0
%define major 0
%define libname %mklibname %name %abi %major
%define develname %mklibname -d %name

Name:           schroedinger
Version:        1.0.9
Release:        %mkrel 1
Summary:        Portable libraries for the high quality Dirac video codec

Group:          Video
License:        LGPL/MIT/MPL
URL:            http://www.diracvideo.org/
Source0:        http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
Patch0: schroedinger-1.0.9-fix-linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-

BuildRequires:  liborc-devel
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

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --disable-static --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make check

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname  -p /sbin/ldconfig
%endif

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
