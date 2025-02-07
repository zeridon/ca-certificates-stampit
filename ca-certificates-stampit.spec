#
# spec file for package ca-certificates-stampit
#
# Copyright (c) 2025 Vladimir Vitkov <vvitkov@ghmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%define					certdir %{_datadir}/pki/trust/anchors
Name:           ca-certificates-stampit
Version:        20250207
Release:        1%{?dist}
Summary:        StampIT root certificates
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://stampit.org/
Source:         StampIT_Global_Root_CA.crt
Source1:        StampIT_Primary_Root_CA.crt
Source2:        StampIT_Global_Root_AESCA.crt
Source3:        StampIT_Global_Qualified_CA.crt
BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  p11-kit-devel
Requires(post): ca-certificates
Requires(postun):ca-certificates
BuildArch:      noarch

%description
This package contains the root certificates from stampit.org

%prep
%setup -qcT

%build

%install
install -d -m 755 %{buildroot}/%{certdir}
for i in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3}; do openssl x509 -in $i -out \
	%{buildroot}%{certdir}/${i##*/}; done

%post
update-ca-certificates || true

%postun
update-ca-certificates || true

%files
%{certdir}

%changelog
* Fri Feb  7 2025 Vladimir Vitkov <vvitkov@gmail.com>
- Initial version of package
