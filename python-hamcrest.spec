%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global modname hamcrest
%global origname PyHamcrest

Name:           python-%{modname}
Version:        1.8.5
Release:        2%{?dist}
Summary:        Hamcrest matchers for Python

License:        BSD
URL:            https://github.com/hamcrest/PyHamcrest
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

# https://github.com/hamcrest/PyHamcrest/commit/4327d0be0ca6adfaec427b96149219a224dc826c
Patch0001:      0001-correct-calling-API-call-with-args.patch
# https://github.com/hamcrest/PyHamcrest/commit/27fd600fb24aacef589feddb06ef1725ca30319b
Patch0002:      0001-Return-result-of-a-deferred-call.patch
# https://github.com/hamcrest/PyHamcrest/commit/37a4d0dbeb9a92b959edfb9b1aceba4eaacf9f78
Patch0003:      0001-Add-boolean-matchers.patch

BuildArch:      noarch

%global _description \
PyHamcrest is a framework for writing matcher objects, allowing you to\
declaratively define "match" rules. There are a number of situations where\
matchers are invaluable, such as UI validation, or data filtering, but it is\
in the area of writing flexible tests that matchers are most commonly used.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  pytest
BuildRequires:  python-six
Requires:       python-six
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-six
Requires:       python2-six
%endif
BuildRequires:  python2-mock

%description -n python2-%{modname} %{_description}

Python 2 version.

%if %{with python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{modname} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{origname}-%{version} -p1

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

%check
# Drop coverage and other presets
mv pytest.ini pytest.ini~
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
%if %{with python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif

%files -n python2-%{modname}
%{python2_sitelib}/%{origname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%if %{with python3}
%files -n python3-%{modname}
%{python3_sitelib}/%{origname}-*.egg-info/
%{python3_sitelib}/%{modname}/
%endif

%changelog
* Sun Aug 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-2
- Backport couple of upstream patches

* Fri Aug 19 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-1
- Initial package
