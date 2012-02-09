%define version	1.2.1
%define release	7
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
BuildRoot:	%{name}-%{version}

Requires:	urpmi	       >= 6.68
Requires:	python-rpm     >= 5.3
Requires:	libxml2-python >= 2.7
Requires:       gzip
Requires:	python-rpm5utils = %{version}

%description
%{name} is a collection of utilities for URPM-base repositories. 
They make URPM-based repositories easier and more powerful to use.
These tools include: urpm-downloader, urpm-package-cleanup, 
urpm-repoclosure, urpm-repodiff, urpm-repomanage, urpm-repograph

%package -n	python-rpm5utils
Group:		Development/Python
Summary:	Auxiliary modules to work with rpm
Provides:	python-rpm5utils = %{version}-%{release}
Obsoletes:	python-rpmutils

%description -n python-rpm5utils
%{name} contains some useful modules that are used by %{name}. 
Mostly taken from yum.

%prep
%setup -q -n %{name}-%{version}

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
%{_bindir}/urpm-repograph
%{_mandir}/man1/urpm-downloader.1.xz
%{_mandir}/man1/urpm-package-cleanup.1.xz
%{_mandir}/man1/urpm-repoclosure.1.xz
%{_mandir}/man1/urpm-repodiff.1.xz
%{_mandir}/man1/urpm-repomanage.1.xz
%{_mandir}/man1/urpm-repograph.1.xz
%doc COPYING

%files -n python-rpm5utils
%defattr(-,root,root,-)
%{py_puresitedir}/urpmmisc.py
%{py_puresitedir}/rpm5Utils/*.py
%{py_puresitedir}/rpm5Utils/*.pyc
%dir %{py_puresitedir}/rpm5Utils
%dir %{py_puresitedir}/rpm5Utils/tests
%{py_puresitedir}/rpm5Utils/tests/*.py
%doc rpm5Utils/COPYING