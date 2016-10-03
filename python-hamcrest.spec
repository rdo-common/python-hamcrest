%global modname hamcrest
%global origname PyHamcrest

Name:           python-%{modname}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Hamcrest matchers for Python

License:        BSD
URL:            https://github.com/hamcrest/PyHamcrest
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

# https://github.com/hamcrest/PyHamcrest/commit/37a4d0dbeb9a92b959edfb9b1aceba4eaacf9f78
Patch0001:      0001-Add-boolean-matchers.patch

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
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  python2-six
Requires:       python2-six

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
%py3_build

%install
%py2_install
%py3_install

%check
# Drop coverage and other presets
mv pytest.ini pytest.ini~
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python2-%{modname}
%{python2_sitelib}/%{origname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%files -n python3-%{modname}
%{python3_sitelib}/%{origname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Mon Oct 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sun Aug 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-2
- Backport couple of upstream patches

* Fri Aug 19 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-1
- Initial package
