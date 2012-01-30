Summary:	monitrc file for monitoring Apache web server
Summary(pl.UTF-8):	Plik monitrc do monitorowania serwera WWW Apache
Name:		monit-rc-apache
Version:	1.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	apache.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	apache-base >= 2.2.3-8
Requires:	monit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Apache web server.

%description -l pl.UTF-8
Plik monitrc do monitorowania serwera WWW Apache.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit/httpd.monitrc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%triggerpostun -- apache < 2.2.0
# rename monitrc to be service name like other files
if [ -f /etc/monit/apache.monitrc.rpmsave ]; then
	mv -f /etc/monit/httpd.monitrc{,.rpmnew}
	mv -f /etc/monit/{apache.monitrc.rpmsave,httpd.monitrc}
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/monit/*.monitrc
