%define abi 1.0
%define major 0
%define libname %mklibname %{name} %{abi} %{major}
%define develname %mklibname -d %{name}

Name:		schroedinger
Version:	1.0.11
Release:	11
Summary:	Portable libraries for the high quality Dirac video codec
Group:		Video
License:	LGPL/MIT/MPL
URL:		http://www.diracvideo.org/
Source0:	http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
Patch0:		schroedinger-1.0.9-fix-linking.patch
Patch1:		schroedinger-automake-1.13.patch

BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	gtk-doc

%track
prog %name = {
	URL = http://www.diracvideo.org/download/schroedinger/
	version = %version
	regex = %name-(__VER__)\.tar\.gz
}

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
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc
%make

%install
%makeinstall_std

%check
make check

%files -n %{libname}
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-%{abi}.so.%{major}*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc



%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.10-3
+ Revision: 744646
- rebuild
- cleaned up spec

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2
+ Revision: 669961
- mass rebuild

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 1.0.10-1mdv2011.0
+ Revision: 591446
- update to new version 1.0.10

* Wed Mar 10 2010 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdv2010.1
+ Revision: 517365
- new version
- fix linking
- build with orc instead of liboil
- enable tests

* Thu Oct 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.8-1mdv2010.0
+ Revision: 452281
- Update to new version 1.0.8
- Gstreamer plug-in now provided by gstreamer0.10-plugins-bad

* Fri May 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.7-1mdv2010.0
+ Revision: 373485
- update to new version 1.0.7

* Sun May 03 2009 Götz Waschk <waschk@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 371155
- new version
- bump deps

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 366284
- use configure2_5x

  + Götz Waschk <waschk@mandriva.org>
    - fix URL

* Wed Jul 02 2008 Götz Waschk <waschk@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 230610
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 23 2008 Götz Waschk <waschk@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 196756
- import schroedinger


* Wed Apr 23 2008 Götz Waschk <waschk@mandriva.org> 1.0.3-1mdv2009.0
- initial package based on the Fedora specy

* Fri Feb 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.0-1
- Update to 1.0.0

* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.9.0-2
- Rebuild for GCC 4.3

* Mon Nov 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.9.0-1
- Update to 0.9.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.6.1-3
- Rebuild for selinux ppc32 issue.

* Wed Jun 20 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.6.1-2
- Fix license field
- Add pkgconfig as a requirement for the devel subpackage

* Sun Jun 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.6.1-1
- First version for Fedora
