%define version	1.0.1
%define release	3
%define name	urpm-tools


Name:           %name
Version:        %version
Release:        %release
Summary:        Utilities that help to work with URPM-based repositories
Group:          System/Configuration/Packaging
License:        LGPLv2
URL:            http://wiki.rosalab.ru/index.php/Urpm-tools
Source0:        %{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	urpmi	       >= 6.68
Requires:	python-rpm     >= 5.3
Requires:	libxml2-python >= 2.7
Requires:       gzip
Requires:	python-rpmutils = %{version}
Conflicts:	yum

%description
%{name} is a collection of utilities for URPM-base repositories. 
They make URPM-based repositories easier and more powerful to use.
These tools include: urpm-downloader, urpm-package-cleanup, 
urpm-repoclosure, urpm-repodiff, urpm-repomanage

%package -n	python-rpmutils
Group:		Development/Python
Summary:	Auxiliary modules to work with rpm
Provides:	python-rpmutils = %{version}-%{release}

%description -n python-rpmutils
%{name} contains some useful modules that are used by %{name}. 
Mostly taken from yum.

%prep
%setup -q -n %{name}

#%build

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)

%{_bindir}/urpm-downloader
%{_bindir}/urpm-package-cleanup
%{_bindir}/urpm-repoclosure
%{_bindir}/urpm-repodiff
%{_bindir}/urpm-repomanage

%{_mandir}/man1/urpm-downloader.1.xz
%{_mandir}/man1/urpm-package-cleanup.1.xz
%{_mandir}/man1/urpm-repoclosure.1.xz
%{_mandir}/man1/urpm-repodiff.1.xz
%{_mandir}/man1/urpm-repomanage.1.xz
%doc COPYING

%files -n python-rpmutils
%defattr(-,root,root,-)
%{py_puresitedir}/urpmmisc.py
%{py_puresitedir}/rpmUtils/*.py
%{py_puresitedir}/rpmUtils/*.pyc
%dir %{py_puresitedir}/rpmUtils
%dir %{py_puresitedir}/rpmUtils/tests
%{py_puresitedir}/rpmUtils/tests/*.py
%doc rpmUtils/COPYING