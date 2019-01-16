%define abi 1.0
%define major 0
%define libname %mklibname %{name} %{abi} %{major}
%define develname %mklibname -d %{name}

Name:		schroedinger
Version:	1.0.11
Release:	18
Summary:	Portable libraries for the high quality Dirac video codec
Group:		Video
License:	LGPL/MIT/MPL
URL:		http://www.diracvideo.org/
Source0:	http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
Patch0:		schroedinger-1.0.9-fix-linking.patch
Patch1:		schroedinger-automake-1.13.patch

BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	gtk-doc

%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package -n %{libname}
Group:		System/Libraries
Summary:	Portable libraries for the high quality Dirac video codec

%description -n %{libname}
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package -n %{develname}
Group:		Development/C
Summary:	Development files for schrodinger
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for schrodinger

%prep
%autosetup -p1
autoreconf -fi

%build
%configure \
	--disable-static \
	--disable-gtk-doc
%make_build

%install
%make_install

%check
make check

%files -n %{libname}
%{_libdir}/libschroedinger-%{abi}.so.%{major}*

%files -n %{develname}
%doc COPYING* NEWS TODO
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc
