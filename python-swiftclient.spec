Name:       python-swiftclient
Version:    1.2.0
Release:    2%{?dist}
Summary:    Python API and CLI for OpenStack Swift

License:    ASL 2.0
URL:        https://github.com/openstack/python-swiftclient
BuildArch:  noarch

#Source0:    https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source0:    http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=1.2.0
#


Requires:   python-simplejson
# /usr/bin/swift collision with swift-im rhbz#857900
Conflicts:  swift

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
%doc LICENSE README.rst
%{_bindir}/swift
%{python_sitelib}/swiftclient
%{python_sitelib}/*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> 1.2.0-2
- conflict with swift-im bz#857900

* Thu Sep 13 2012 Alan Pevec <apevec@redhat.com> 1.2.0-1
- Update to 1.2.0 release.

* Tue Jul 31 2012 Alan Pevec <apevec@redhat.com> 1.1.1-1
- Initial release.
