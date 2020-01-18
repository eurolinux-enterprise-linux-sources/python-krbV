%{!?python_sitearch: %global python_sitearch %([ -x %{__python} ] && %{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" || :)}

Name: python-krbV
Version: 1.0.90
Release: 6%{?dist}
Summary: Python extension module for Kerberos 5

Group: Development/Languages
License: LGPLv2+

URL: http://fedorahosted.org/python-krbV/
Source: https://fedorahosted.org/python-krbV/raw-attachment/wiki/Releases/python-krbV-%{version}.tar.bz2

BuildRequires: python-devel
BuildRequires: krb5-devel >= 1.2.2
BuildRequires: /bin/awk

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
python-krbV allows python programs to use Kerberos 5 authentication and security.

%prep
%setup -q

%build
export LIBNAME="%{_lib}"
export CFLAGS="%{optflags} -Wextra"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}/%{python_sitearch}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING krbV-code-snippets.py
%{python_sitearch}/krbVmodule.so

%changelog
* Mon Nov 19 2012 John Dennis <jdennis@redhat.com> - 1.0.90-6
- fix upstream source url

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Mike Bonnet <mikeb@redhat.com> - 1.0.90-3
- rebuild for krb5-1.9

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue May 18 2010 Mike Bonnet <mikeb@redhat.com> - 1.0.90-1
- return the contents of the AP_REP message from rd_rep()
- improved memory handling
- removed use of KRB_PRIVATE

* Mon Jan 18 2010 Mike Bonnet <mikeb@redhat.com> - 1.0.14-1
- new release with better docstrings

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.13-8
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.13-7
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Mike Bonnet <mikeb@redhat.com> - 1.0.13-6
- rebuild for F8

* Mon Dec 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-5
- rebuild for python 2.5
- remove obsolete python-abi Requires:

* Wed Sep 13 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-4
- support building against krb5-1.5, where the headers have been moved to /usr/include/krb5

* Mon Sep 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-3
- rebuild for FC6

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-2
- spec file cleanup

* Wed May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-1
- AuthContext.addrs can now be set manually, rather than calling genaddrs()

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-3
- use macros consistently

* Thu Apr 27 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-2
- configure.in: parse version number out of spec file
- add URL tag
- add LGPL text
- remove Requires: krb5-libs, let rpm pick up library dependencies
- bump revision

* Mon Apr 24 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-1
- bump version number due to API changes

* Fri Mar 24 2006 Mike Bonnet <mikeb@redhat.com>
- fix typo in error definition
- change the return value of recvauth() from ac to (ac, princ), where princ is the principal sent by sendauth()
- rename the package and reorganize the BuildRequires, to be more Extras-friendly

* Tue Sep 25 2001 Elliot Lee <sopwith@redhat.com>
- Initial version
