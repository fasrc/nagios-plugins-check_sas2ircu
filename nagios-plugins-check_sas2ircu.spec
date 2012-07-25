Name:		nagios-plugins-check_sas2ircu
Version:	92d3a1
Release:	1%{?dist}
Summary:	Nagios plugin that checks LSI SAS2 controllers RAID status via sas2ircu program
License:	GPL
URL:		http://exchange.nagios.org/directory/Plugins/Hardware/Storage-Systems/RAID-Controllers/check_sas2ircu/details
#Source0:	http://git.home-dn.net/?p=manu/check_sas2ircu.git;a=blob_plain;f=check_sas2ircu;h=92d3a1789c7f8a2af5917ba183b530bf5012bd08;hb=f23db38391bf2fafc9ea939a723644e6c46e2925
Source0:	check_sas2ircu
Patch0:		nagios-plugins-check_sas2ircu-92d3a1.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Nagios plugin that checks LSI SAS2 controllers RAID status via sas2ircu program

%prep
rm -rf %{_builddir}/%{name}-%{version}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cp "%{SOURCE0}" %{_builddir}/%{name}-%{version}
%patch0 -p0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/nagios/plugins
cp %{_builddir}/%{name}-%{version}/check_sas2ircu %{buildroot}%{_libdir}/nagios/plugins/check_sas2ircu

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc
%attr(0755, root, root) %{_libdir}/nagios/plugins/check_sas2ircu

%changelog
* Wed Jul 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 92d3a1-1
- Initial package
