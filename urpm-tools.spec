Name:           urpm-tools
Version:        2.2.6
Release:        2
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
%setup -qn %{name}

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/urpm*
%{_mandir}/man1/*

%doc COPYING

%files -n python-rpm5utils
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
