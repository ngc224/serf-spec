Summary: Service orchestration and management tool
Name: serf
Version: 0.5.0
Release: 1
License: Mozilla Public License, version 2.0
Group: System Environment/Base
Source0: https://dl.bintray.com/mitchellh/serf/%{version}_linux_amd64.zip
URL: http://www.serfdom.io/

BuildRoot: %{_tmppath}/%{name}-root

%description
Serf is a decentralized solution for service discovery and orchestration that is lightweight, highly available, and fault tolerant.

%prep
%setup -T -c
unzip -o %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 serf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Mon Mar 17 2013 Yoshihiko Nishida <nishida@ngc224.org> - 6-5.el6.centos
- Build for CentOS-6.5
