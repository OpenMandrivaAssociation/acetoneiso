Name:		acetoneiso
Version:	2.2.2
Release:	%mkrel 1
Summary:	CD/DVD Image Manipulator
Group:		Archiving/Other
License:	GPLv3
URL:		http://www.acetoneteam.org/
Source0:	http://download.sourceforge.net/acetoneiso/%{name}_%{version}.tar.gz
Patch1:		fix_phonon_includes.patch
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: 	qt4-devel, desktop-file-utils
Requires:	p7zip, cdrdao, fuseiso, fuse, cdrkit-genisoimage, gnupg, pinentry-qt4

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
%patch1 -p0

%build
cd %{name}/
%qmake_qt4
%make

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
