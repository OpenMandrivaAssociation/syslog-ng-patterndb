%define	name	syslog-ng-patterndb
%define	version	20091209
%define release	3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Syslog-ng pattern database
License:    GPL
Group:      Graphical desktop/GNOME
URL:        http://www.balabit.com/downloads/files/patterndb-snapshot
Source0:    http://www.balabit.com/downloads/files/patterndb-snapshot/patterndb-%{version}.zip
BuildArch:      noarch

%description
This package contains a pattern database for syslog-ng.

%prep
%setup -q -n patterndb

%build

%install
install -d -m 755 %{buildroot}%{_datadir}/syslog-ng
install -m 644 *.xml %{buildroot}%{_datadir}/syslog-ng

%files
%{_datadir}/syslog-ng
