%define	name	syslog-ng-patterndb
%define	version	20091209
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Syslog-ng pattern database
License:    GPL
Group:      Graphical desktop/GNOME
URL:        http://www.balabit.com/downloads/files/patterndb-snapshot
Source0     http://www.balabit.com/downloads/files/patterndb-snapshot/patterndb-%{version}.zip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This package contains a pattern database for syslog-ng.

%prep
%setup -q -n patterndb

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/syslog-ng
install -m 644 *.xml %{buildroot}%{_datadir}/syslog-ng

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/syslog-ng

