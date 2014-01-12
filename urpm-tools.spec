Name:           urpm-tools
Version:        2.2.4
Release:        4
Summary:        Utilities that help to work with URPM-based repositories
Group:          System/Configuration/Packaging
License:        GPLv2
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
%{name} is a collection of utilities for URPM-based repositories. 
They make URPM-based repositories easier and more powerful to use.
These tools include: urpm-downloader, urpm-package-cleanup, 
urpm-repoclosure, urpm-repodiff, urpm-repomanage, urpm-repograph,
urpm-reposync

%package -n	python-rpm5utils
Group:		Development/Python
Summary:	Auxiliary modules to work with rpm
Provides:	python-rpm5utils = %{version}-%{release}

%description -n python-rpm5utils
%{name} contains some useful modules that are used by %{name}. 
Mostly taken from yum.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)

%{_bindir}/urpm-downloader
%{_bindir}/urpm-package-cleanup
%{_bindir}/urpm-repoclosure
%{_bindir}/urpm-repodiff
%{_bindir}/urpm-repomanage
%{_bindir}/urpm-repograph
%{_bindir}/urpm-reposync
%{_mandir}/man1/urpm-downloader.1.xz
%{_mandir}/man1/urpm-package-cleanup.1.xz
%{_mandir}/man1/urpm-repoclosure.1.xz
%{_mandir}/man1/urpm-repodiff.1.xz
%{_mandir}/man1/urpm-repomanage.1.xz
%{_mandir}/man1/urpm-repograph.1.xz
%{_mandir}/man1/urpm-reposync.1.xz

#%{_datadir}/locale/*/LC_MESSAGES/urpm-tools.mo
%doc COPYING

%files -n python-rpm5utils
%defattr(-,root,root,-)
%dir %{py_puresitedir}/rpm5utils
%dir %{py_puresitedir}/rpm5utils/tests
%dir %{py_puresitedir}/rpm5utils/urpmgraphs
%dir %{py_puresitedir}/rpm5utils/urpmgraphs/algorithms
%dir %{py_puresitedir}/rpm5utils/urpmgraphs/algorithms/components
%dir %{py_puresitedir}/rpm5utils/urpmgraphs/classes

%{py_puresitedir}/urpmmisc.py
%{py_puresitedir}/rpm5utils/*.py*
%{py_puresitedir}/rpm5utils/tests/*.py*
%{py_puresitedir}/rpm5utils/urpmgraphs/*.py*
%{py_puresitedir}/rpm5utils/urpmgraphs/algorithms/*.py*
%{py_puresitedir}/rpm5utils/urpmgraphs/algorithms/components/*.py*
%{py_puresitedir}/rpm5utils/urpmgraphs/classes/*.py*

%doc rpm5utils/COPYING
