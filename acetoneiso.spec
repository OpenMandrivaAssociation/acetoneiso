Name:		acetoneiso
Version:	2.2.1
Release:	%mkrel 1
Summary:	CD/DVD Image Manipulator
Group:		Archiving/Other
License:	GPLv3
URL:		http://www.acetoneteam.org/
Source0:	http://download.sourceforge.net/sourceforge/acetoneiso2/%{name}_%{version}.tar.bz2
Patch0:		acetoneiso-2.1.1-desktop.patch
Patch1:		fix_phonon_includes.patch
#Patch1:		AcetoneISO2-2.0.3-no-poweriso-for-non-x86.patch
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: 	kdewebdev4-devel, qt4-devel, desktop-file-utils
Requires:	p7zip, cdrdao, fuseiso, fuse, cdrkit-genisoimage, gnupg, pinentry-qt4
#Provides:	acetoneiso

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
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1

%build
cd %{name}/
qmake
make LFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT 
cd %{name}/
make INSTALL_ROOT=$RPM_BUILD_ROOT install
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/AcetoneISO.desktop

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG FEATURES LICENSE README
%{_bindir}/acetoneiso
%{_datadir}/applications/AcetoneISO.desktop
%{_datadir}/pixmaps/Acetino2.png
