%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-sahara
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Sahara
License:        ASL 2.0

URL:            https://launchpad.net/puppet-sahara

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
#Requires:       puppet-postgresql
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet-sysctl
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Sahara

%prep
%setup -q -n openstack-sahara-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/sahara/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/sahara/



%files
%{_datadir}/openstack-puppet/modules/sahara/


%changelog


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-sahara/commit/?id=7623634cb2137fa829cefc90945f20d8ded64a9a
