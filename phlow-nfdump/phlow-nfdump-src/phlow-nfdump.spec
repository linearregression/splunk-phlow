Name:			phlow-nfdump
Version:		0.10
Release:		1%{?dist}
Summary:		Netflow processing tools	

Group:			System Environment/Daemons
License:		BSD
URL:			https://github.com/phlowy
Source0:		%{name}-%{version}.tar.gz
BuildRoot:		%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		bison
BuildRequires:		flex
BuildRequires:		rrdtool-devel
Requires(pre):		/usr/sbin/useradd, /usr/bin/getent, /usr/sbin/groupadd, /sbin/nologin 
Requires(pre):		inotify-tools
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
	/bin/mkdir /var/log/nfcapd
	/bin/mkdir /var/log/nfdump-ascii
	/bin/chown nfcapd:nfcapd /var/log/nfcapd
	/bin/chown nfcapd:nfcapd /var/log/nfdump-ascii
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
%{__mkdir_p} %{buildroot}/etc/logrotate.d/
%{__mkdir_p} %{buildroot}/usr/bin/
%{__install} -pm0644 src/etc/nfcapd.conf %{buildroot}%{_sysconfdir}/nfcapd.conf
%{__install} -pm0755 src/etc/init.d/nfcapd %{buildroot}%{_sysconfdir}/init.d/nfcapd
%{__install} -pm0755 src/etc/init.d/nfdump-ascii %{buildroot}%{_sysconfdir}/init.d/nfdump-ascii
%{__install} -pm0644 src/etc/sysconfig/nfcapd %{buildroot}%{_sysconfdir}/sysconfig/nfcapd
%{__install} -pm0755 src/etc/cron.hourly/nfcapd.cron %{buildroot}%{_sysconfdir}/cron.hourly/nfcapd.cron
%{__install} -pm0644 src/etc/logrotate.d/nfdump-ascii %{buildroot}%{_sysconfdir}/logrotate.d/nfdump-ascii
%{__install} -pm0755 src/usr/bin/nfdump-ascii.sh %{buildroot}%{_prefix}/bin/nfdump-ascii.sh
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
%attr(755,root,root) %{_sysconfdir}/init.d/nfdump-ascii
%{_sysconfdir}/sysconfig/nfcapd
%attr(755,root,root) %{_sysconfdir}/cron.hourly/nfcapd.cron
%{_sysconfdir}/logrotate.d/nfdump-ascii
%attr(755,root,root) %{_prefix}/bin/nfdump-ascii.sh

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add nfcapd
/sbin/service nfcapd start >/dev/null 2>&1
echo " "
echo "Please read /etc/sysconfig/nfcapd"
echo " "
echo "for instruction on separating netflows"
echo " "
echo "in directories based on the source device "
echo " "
echo " "
/sbin/chkconfig --add nfdump-ascii
/sbin/service nfdump-ascii start >/dev/null 2>&1

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service nfcapd stop >/dev/null 2>&1
	/sbin/chkconfig --del nfcapd
	/sbin/service nfdump-ascii stop >/dev/null 2>&1
	/sbin/chkconfig --del nfdump-ascii
	/bin/rm -rf /var/log/nfcapd
	/bin/rm -rf /var/log/nfdump-ascii
	/usr/sbin/userdel nfcapd
fi

%postun
if [ $1 -eq 1 ] ; then
	/sbin/service nfcapd condrestart >/dev/null 2>&1 || :
	/sbin/service nfdump-ascii  >/dev/null 2>&1 || :
fi

%changelog
* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.10-1
- add install of nfdump-ascii.sh

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.9-1
- correct syntax errors in spec file

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.8-1
- add create /var/log/ directories to spec file

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.7-1
- 

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.6-1
- update & correct syntax issues (jcwx@inoc.com)

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.5-1
- copied init scripts from production system

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.4-1
- add phlow-nfdump comment and description to
- README file

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.3-1
- correct spec file, add nfdump-ascii init write

* Wed Apr 24 2013 jcwx <jcwx@inoc.com> 0.2-1
- new package built with tito

