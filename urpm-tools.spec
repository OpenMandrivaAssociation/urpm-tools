Name:		urpm-tools
Version:	2.3.3
Release:	0.1
Summary:	Utilities that help to work with URPM-based repositories
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/index.php/Urpm-tools
Source0:	https://abf.io/soft/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	urpmi	       >= 6.68
Requires:	python-rpm     >= 5.3
Requires:	libxml2-python >= 2.7
Requires:	gzip
Requires:	python-rpm5utils = %{EVRD}

%description
%{name} is a collection of utilities for URPM-based repositories. 
They make URPM-based repositories easier and more powerful to use.
These tools include: urpm-downloader, urpm-package-cleanup, 
urpm-repoclosure, urpm-repodiff, urpm-repomanage, urpm-repograph,
urpm-reposync

%package -n python-rpm5utils
Group:		Development/Python
Summary:	Auxiliary modules to work with rpm
Provides:	python-rpm5utils = %{EVRD}

%description -n python-rpm5utils
%{name} contains some useful modules that are used by %{name}.
Mostly taken from yum.

%prep
%setup -q

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/urpm*
%{_mandir}/man1/*

%doc COPYING

%files -n python-rpm5utils
%dir %{python_sitelib}/rpm5utils
%dir %{python_sitelib}/rpm5utils/tests
%dir %{python_sitelib}/rpm5utils/urpmgraphs
%dir %{python_sitelib}/rpm5utils/urpmgraphs/algorithms
%dir %{python_sitelib}/rpm5utils/urpmgraphs/algorithms/components
%dir %{python_sitelib}/rpm5utils/urpmgraphs/classes

%{python_sitelib}/urpmmisc.py
%{python_sitelib}/rpm5utils/*.py*
%{python_sitelib}/rpm5utils/tests/*.py*
%{python_sitelib}/rpm5utils/urpmgraphs/*.py*
%{python_sitelib}/rpm5utils/urpmgraphs/algorithms/*.py*
%{python_sitelib}/rpm5utils/urpmgraphs/algorithms/components/*.py*
%{python_sitelib}/rpm5utils/urpmgraphs/classes/*.py*

%doc rpm5utils/COPYING
