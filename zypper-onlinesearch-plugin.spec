#
# spec file for package zypper-onlinesearch-plugin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-onlinesearch-plugin
Version:        1.0.0
Release:        0
%define mod_name zypper-onlinesearch
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       rubygem(zypper-onlinesearch)
Requires:       zypper >= 1.13.10
Url:            https://github.com/fabiomux/zypper-onlinesearch-plugin
Source:         %{mod_full_name}.tgz
Summary:        Zypper plugin that search for packages through dedicated directory search engines
License:        GPL-3.0
Group:          System/Packages

%description
A zypper plugin which enables the package research through online search
engines like software.opensuse.org and Packman.

%prep
%setup -q -n %{mod_name}

%build

%install
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 755 zypper-onlinesearch %{buildroot}/usr/lib/zypper/commands/
install -m 644 zypper-onlinesearch.8 %{buildroot}/%{_mandir}/man8/

%files
%defattr(-,root,root,-)
/usr/lib/zypper
/usr/lib/zypper/commands
%{_mandir}/man8/*


%changelog
