#
# Conditional build:
%bcond_without	python2
%bcond_with	python3 # it seems it is not there, although 'six' is used

Summary:	Eucalyptus/AWS-compatible command line tools
Summary(pl.UTF-8):	Narzędzia linii poleceń zgodne z Eucalyptus/AWS
Name:		euca2ools
Version:	3.2.0
Release:	3
License:	BSD
Group:		Applications/Networking
Source0:	http://downloads.eucalyptus.com/software/euca2ools/3.2/source/%{name}-%{version}.tar.xz
# Source0-md5:	b62502aa45f679c4f0ad01b658f095f5
URL:		https://github.com/eucalyptus/euca2ools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools > 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-setuptools > 1:7.0
%endif
Requires:	gdisk
Requires:	gzip
Requires:	kpartx
Requires:	openssl-tools
Requires:	parted
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-modules
Requires:	rsync
Requires:	util-linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Euca2ools are command line tools used to interact with Amazon Web
Services (AWS) as well as other compatible services, such as
Eucalyptus. They aim to use the same input as similar tools provided
by AWS for each service individually along with several enhancements
that make them easier to use.

%description -l pl.UTF-8
Euca2ools to narzędzia linii poleceń służące do pracy z usługami AWS
(Amazon Web Services) oraz innymi zgodnymi, takimi jak Eucalyptus.
Celem jest używanie takiego samego wejścia, jak podobne narzędzia
dostarczane przez AWS do poszczególnych usług z kilkoma rozszerzeniami
ułatwiającymi ich używanie.

%package -n python-%{name}
Summary:	Euca2ools Python 2 modules
Summary(pl.UTF-8):	Moduły Pythona 2 Euca2ools
Group:		Libraries/Python
Requires:	python-lxml
Requires:	python-progressbar
Requires:	python-requestbuilder
Requires:	python-requests
Requires:	python-setuptools
Requires:	python-six

%description -n python-%{name}
Euca2ools Python 2 modules.

%description -n python-%{name} -l pl.UTF-8
Moduły Pythona 2 Euca2ools.

%package -n python3-%{name}
Summary:	Euca2ools Python 3 modules
Summary(pl.UTF-8):	Moduły Pythona 3 Euca2ools
Group:		Libraries/Python
Requires:	python3-lxml
Requires:	python3-progressbar
Requires:	python3-requestbuilder
Requires:	python3-requests
Requires:	python3-setuptools
Requires:	python3-six

%description -n python3-%{name}
Euca2ools Python 3 modules.

%description -n python3-%{name} -l pl.UTF-8
Moduły Pythona 3 Euca2ools.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL
%attr(755,root,root) %{_bindir}/euare-*
%attr(755,root,root) %{_bindir}/euca-*
%attr(755,root,root) %{_bindir}/euform-*
%attr(755,root,root) %{_bindir}/eulb-*
%attr(755,root,root) %{_bindir}/euscale-*
%attr(755,root,root) %{_bindir}/euwatch-*
%{_mandir}/man1/euare-*.1*
%{_mandir}/man1/euca-*.1*
%{_mandir}/man1/euform-*.1*
%{_mandir}/man1/eulb-*.1*
%{_mandir}/man1/euscale-*.1*
%{_mandir}/man1/euwatch-*.1*

%if %{with python2}
%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}-%{version}-py*.egg-info
%endif
