Name:			ise-nfdump
Version:		0.7.19
Release:		1%{?dist}
Summary:		Netflow processing tools	

Group:			System Environment/Daemons
License:		BSD
URL:			http://gitorious.inf.ise.com/
Source0:		%{name}-%{version}.tar.gz
BuildRoot:		%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		bison
BuildRequires:		flex
BuildRequires:		rrdtool-devel
Requires(pre):		/usr/sbin/useradd, /usr/bin/getent, /usr/sbin/groupadd, /sbin/nologin 
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	/usr/sbin/userdel

%description
The nfdump tools collect and process netflow data

# from Fedora rpm guidelines
# used to identify what stage is involved in if-then statements
#
#          install   erase   upgrade  reinstall
#%pre         1        -         2         2
#%post        1        -         2         2
#%preun       -        0         1         -
#%postun      -        0         1         -

%pre
if [ $1 -eq 1 ] ; then
	/usr/bin/getent group nfcapd >/dev/null || /usr/sbin/groupadd -r nfcapd
	/usr/bin/getent passwd nfcapd >/dev/null || \
	/usr/sbin/useradd -r -g nfcapd -d /home/nfcapd \
	-s /sbin/nologin -c "used for nfcapd daemon (nfdump)" nfcapd
exit 0
fi

%prep
%setup -q


%build
%configure \
	--enable-nfprofile \
	--enable-sflow
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}/etc/sysconfig/
%{__mkdir_p} %{buildroot}/etc/init.d/
%{__mkdir_p} %{buildroot}/etc/cron.hourly/
%{__install} -pm0644 src/etc/nfcapd.conf %{buildroot}%{_sysconfdir}/nfcapd.conf
%{__install} -pm0755 src/etc/init.d/nfcapd %{buildroot}%{_sysconfdir}/init.d/nfcapd
%{__install} -pm0644 src/etc/sysconfig/nfcapd %{buildroot}%{_sysconfdir}/sysconfig/nfcapd
%{__install} -pm0755 src/etc/cron.hourly/nfcapd.cron %{buildroot}%{_sysconfdir}/cron.hourly/nfcapd.cron
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
#%defattr(-,root,root,-)
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/nf*
%attr(755,root,root) %{_bindir}/sfcapd
%{_mandir}/man1/*
%{_sysconfdir}/nfcapd.conf
%attr(755,root,root) %{_sysconfdir}/init.d/nfcapd
%{_sysconfdir}/sysconfig/nfcapd
%attr(755,root,root) %{_sysconfdir}/cron.hourly/nfcapd.cron

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add nfcapd
echo " "
echo "Please note:"
echo " "
echo "add/change IP addresses in /etc/nfcapd.conf"
echo " "
echo "then start the daemon with 'service nfcapd start' "
echo " "
echo " "

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service nfcapd stop >/dev/null 2>&1
	/sbin/chkconfig --del nfcapd
	/bin/rm -rf /var/log/nfcapd
	/usr/sbin/userdel nfcapd
fi

%postun
if [ $1 -eq 1 ] ; then
	/sbin/service nfcapd condrestart >/dev/null 2>&1 || :
fi

%changelog
* Fri Feb 22 2013 jcwx <jcwx@inoc.com> 0.7.19-1
- change log write to 5 minutes

* Fri Feb 01 2013 jcwx <jcwx@inoc.com> 0.7.18-1
- remove compression flag from daemon config string

* Wed Jan 23 2013 jcwx <jcwx@inoc.com> 0.7.17-1
- change install note
- adjust nfcapd init flags

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.16-1
- correct ANOTHER syntax error

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.15-1
- correct syntax

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.14-1
- edited install note

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.13-1
- move echoed post install instructions

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.12-1
- correct syntax error in spec file

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.11-1
- add edit note to spec file
- change nfexpire log cycle to 6 days

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.10-1
- add ISE firewall IPs to nfcapd.conf
- corrected scriptlet if-then statements

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.9-1
- add condrestart function to init script

* Sun Jan 13 2013 jcwx <jcwx@inoc.com> 0.7.8-1
- add if-then statements for scriptlets
- change log cycle to 1 minute

* Sat Jan 12 2013 jcwx <jcwx@inoc.com> 0.7.7-1
- remove logrotate config
- add nfexpire config

* Fri Jan 11 2013 jcwx <jcwx@inoc.com> 0.7.6-1
- change logrotate parameters

* Fri Jan 11 2013 jcwx <jcwx@inoc.com> 0.7.5-1
- add files definition for logrotate

* Fri Jan 11 2013 jcwx <jcwx@inoc.com> 0.7.4-1
- add logrotate config
- delete /var/log/nfcapd on rpm erase

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.7.3-1
- more corrections

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.7.2-1
- more corrections

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.7.1-1
- syntax corrections

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.7.0-1
- add init file, add config files

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.6.0-1
-  add config options

* Thu Jan 10 2013 jcwx <jcwx@inoc.com> 0.5.0-1
- add more files

* Wed Jan 09 2013 jcwx <jcwx@inoc.com> 0.4.0-1
- remove config flags

* Wed Jan 09 2013 jcwx <jcwx@inoc.com> 0.3.0-1
- add source code

* Mon Jan 07 2013 jcwx <jcwx@inoc.com> 0.2.0-1
- add attributes for files

* Fri Jan 04 2013 jcwx <jcwx@inoc.com> 0.1.0-1
- new package built with tito

