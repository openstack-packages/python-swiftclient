Name:       python-swiftclient
Version:    1.1.1
Release:    1%{?dist}
Summary:    Python API and CLI for OpenStack Swift

License:    ASL 2.0
URL:        https://github.com/openstack/python-swiftclient
BuildArch:  noarch

Source0:    https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz

#
# patches_base=1.1.1
#
Patch0001: 0001-Now-url-encodes-decodes-x-object-manifest-values.patch
Patch0002: 0002-Removes-the-title-Swift-Web-from-landing-page.patch
Patch0003: 0003-Consume-version-info-from-pkg_resources.patch


Requires:   python-simplejson

BuildRequires: python2-devel
BuildRequires: python-setuptools

%description
Client library and command line utility for interacting with Openstack
Swift's API.

%package doc
Summary:    Documentation for OpenStack Swift API Client
Group:      Documentation

BuildRequires: python-sphinx

%description doc
Documentation for the client library for interacting with Openstack
Swift's API.

%prep
%setup -q
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc README.rst
%{_bindir}/swift
%{python_sitelib}/swiftclient
%{python_sitelib}/*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Jul 31 2012 Alan Pevec <apevec@redhat.com> 1.1.1-1
- Initial release.
