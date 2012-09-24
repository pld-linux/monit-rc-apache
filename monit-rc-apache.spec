Summary:	monitrc file for monitoring Apache web server
Summary(pl.UTF-8):	Plik monitrc do monitorowania serwera WWW Apache
Name:		monit-rc-apache
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	apache.monitrc
Source1:	apache.cron
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	apache-base >= 2.2.3-8
Requires:	monit
Suggests:	crondaemon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Apache web server.

%description -l pl.UTF-8
Plik monitrc do monitorowania serwera WWW Apache.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/monit,/etc/cron.d}

cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit/httpd.monitrc
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/%{name}

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
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
