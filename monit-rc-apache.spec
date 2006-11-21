Summary:	monitrc file for monitoring Apache web server
Summary(pl):	Plik monitrc do monitorowania serwera WWW Apache
Name:		monit-rc-apache
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	apache.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache-base >= 2.2.3-8
Requires:	monit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Apache web server.

%description -l pl
Plik monitrc do monitorowania serwera WWW Apache.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit
install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%{_sysconfdir}/monit/*.monitrc
