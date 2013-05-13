Name:       python-swiftclient
Version:    1.4.0
Release:    1%{?dist}
Summary:    Client Library for OpenStack Object Storage API
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/%{name}
Source0:    http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=1.4.0
#

BuildArch:  noarch
Requires:   python-simplejson
# /usr/bin/swift collision with older swift-im rhbz#857900
Conflicts:  swift < 2.0-0.3

BuildRequires: python2-devel
BuildRequires: python-setuptools

%description
Client library and command line utility for interacting with Openstack
Object Storage API.

%package doc
Summary:    Documentation for OpenStack Object Storage API Client
Group:      Documentation

BuildRequires: python-sphinx

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.

%prep
%setup -q
# Remove bundled egg-info
rm -rf python_swiftclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

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
* Mon May 13 2013 Jakub Ruzicka <jruzicka@redhat.com> 1.4.0-1
- Update to upstream 1.4.0 release.

* Sat Mar 09 2013 Alan Pevec <apevec@redhat.com> 1.3.0-1
- Update to 1.3.0 release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> 1.2.0-2
- conflict with swift-im bz#857900

* Thu Sep 13 2012 Alan Pevec <apevec@redhat.com> 1.2.0-1
- Update to 1.2.0 release.

* Tue Jul 31 2012 Alan Pevec <apevec@redhat.com> 1.1.1-1
- Initial release.
