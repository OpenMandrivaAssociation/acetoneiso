%global enable_debug 0
%global debug_package %{nil}

Name:		acetoneiso
Version:	2.4
Release:	1
Summary:	CD/DVD Image Manipulator
Group:		Archiving/Other
License:	GPLv3
URL:		http://www.acetoneteam.org/
Source0:	http://download.sourceforge.net/acetoneiso/%{name}_%{version}.tar.gz
Patch1:		acetoneiso-2.4-mga-youtube-metacafe.patch
Patch2:		acetoneiso-2.4-size-localized-strings.patch
Patch3:		acetoneiso-2.4-qt5.patch
Patch4:		acetoneiso-2.4-deb-add_manpage.patch
Patch5:		acetoneiso-2.4-deb-remove_defunct_homepage.patch
Patch6:		acetoneiso-cd-mimetype.patch
BuildRequires:	qt5-devel
BuildRequires:	phonon4qt5-devel
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	desktop-file-utils
BuildRequires:	lib64qt5opengl-devel
Requires:	p7zip
Requires:	cdrdao
Requires:	fuseiso
Requires:	fuse
Requires:	cdrkit-genisoimage
Requires:	gnupg
Requires:	pinentry-qt5

%description
AcetoneISO2: The CD/DVD image manipulator for Linux, it can do the following:
- Mount and Unmount ISO, MDF, NRG (if iso-9660 standard)
- Convert / Extract / Browse to ISO : *.bin *.mdf *.nrg *.img *.daa *.cdi 
  *.xbx *.b5i *.bwi *.pdi
- Play a DVD Movie ISO with most commonly-used media players
- Generate an ISO from a Folder or CD/DVD
- Generate/Check MD5 file of an image
- Encrypt/decrypt an image
- Split image into X megabyte chunks
- Highly compress an image
- Rip a PSX cd to *.bin to make it work with epsxe/psx emulators
- Restore a lost CUE file of *.bin *.img

%prep
%setup -q -n %{name}%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%%patch6 -p1
      
%build
cd %{name}/
# Update translations first after we used patch for .ts
#lrelease ./locale/*.ts
%qmake_qt5
sed -i 's|-I/usr/include/QtCore|-I/usr/include/qt5/QtCore -I/usr/include/qt5/KDE|' Makefile

%make

%install
cd %{name}/

make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/AcetoneISO.desktop

%files
%doc AUTHORS CHANGELOG FEATURES LICENSE README
%{_bindir}/acetoneiso
%{_datadir}/applications/AcetoneISO.desktop
%{_datadir}/pixmaps/Acetino2.png


