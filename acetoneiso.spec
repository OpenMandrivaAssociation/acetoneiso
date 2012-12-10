Name:		acetoneiso
Version:	2.3
Release:	%mkrel 2
Summary:	CD/DVD Image Manipulator
Group:		Archiving/Other
License:	GPLv3
URL:		http://www.acetoneteam.org/
Source0:	http://download.sourceforge.net/acetoneiso/%{name}_%{version}.tar.gz
Patch1:		fix_phonon_includes.patch
Patch2:		acetoneiso-2.3-ru.patch
BuildRequires:	qt4-devel
BuildRequires:	phonon-devel
BuildRequires:	desktop-file-utils
Requires:	p7zip
Requires:	cdrdao
Requires:	fuseiso
Requires:	fuse
Requires:	cdrkit-genisoimage
Requires:	gnupg
Requires:	pinentry-qt4

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
%patch2 -p1

%build
cd %{name}/
# Update translations first after we used patch for .ts
lrelease ./locale/*.ts
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
cd %{name}/
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/AcetoneISO.desktop

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG FEATURES LICENSE README
%{_bindir}/acetoneiso
%{_datadir}/applications/AcetoneISO.desktop
%{_datadir}/pixmaps/Acetino2.png


%changelog
* Thu Jan 26 2012 Andrey Bondrov <abondrov@mandriva.org> 2.3-2mdv2011.0
+ Revision: 769120
- Fix BuildRequires (add phonon-devel)
- Add patch with russian translation, spec cleanup

* Mon Nov 29 2010 Juan Luis Baptiste <juancho@mandriva.org> 2.3-1mdv2011.0
+ Revision: 603057
- Updated to 2.3

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 582936
- New version 2.2.2

* Wed Dec 23 2009 Juan Luis Baptiste <juancho@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 481910
- Patch to fix phonon includes in some sources.
- Updated to 2.2.1. Needed patch to fix phonon includes in some sources.

* Tue Sep 22 2009 Juan Luis Baptiste <juancho@mandriva.org> 2.1.1-1mdv2010.0
+ Revision: 447103
- Initial import based on mandrivauser.de package.


