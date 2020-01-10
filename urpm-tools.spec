Name:		urpm-tools
Version:	2.3.3
Release:	4
Summary:	Utilities that help to work with URPM-based repositories
Group:		System/Configuration/Packaging
License:	GPLv2
URL:		http://wiki.rosalab.ru/index.php/Urpm-tools
Source0:	https://abf.io/soft/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:		urpm-tools-use-python2.patch
Patch1:		cz-is-xz-cooker.patch
Patch2:		recognize-lzma-as-xz-hack.patch
Patch3:		dnotrun-file-deps.patch
# (tpg) patches from Rosa
Patch4:		3debe8129f0d6721ab5b6425b6bb7612a55d5982.patch
Patch5:		b9911a08453d2b498524ef17220599a5fbdbd16d.patch
BuildArch:	noarch
Requires:	urpmi >= 6.68
Requires:	python-rpm >= 5.3
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
%autopatch -p1
sed -i -e 's,%{_bindir}/python$,%{_bindir}/python2,g;s,%{_bindir}/python ,%{_bindir}/python2 ,g' *.py

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/urpm*
%{_mandir}/man1/*

%doc COPYING

%files -n python-rpm5utils
%dir %{python2_sitelib}/rpm5utils
%dir %{python2_sitelib}/rpm5utils/tests
%dir %{python2_sitelib}/rpm5utils/urpmgraphs
%dir %{python2_sitelib}/rpm5utils/urpmgraphs/algorithms
%dir %{python2_sitelib}/rpm5utils/urpmgraphs/algorithms/components
%dir %{python2_sitelib}/rpm5utils/urpmgraphs/classes

%{python2_sitelib}/urpmmisc.py
%{python2_sitelib}/rpm5utils/*.py*
%{python2_sitelib}/rpm5utils/tests/*.py*
%{python2_sitelib}/rpm5utils/urpmgraphs/*.py*
%{python2_sitelib}/rpm5utils/urpmgraphs/algorithms/*.py*
%{python2_sitelib}/rpm5utils/urpmgraphs/algorithms/components/*.py*
%{python2_sitelib}/rpm5utils/urpmgraphs/classes/*.py*

%doc rpm5utils/COPYING
