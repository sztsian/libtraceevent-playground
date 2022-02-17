# git tag
#%%global commit 5dd505f3aba255c5fbc2a6dbed57fcba51b400f6
#%%global commitdate 20201009
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name: libtraceevent
Version: 1.5.0
Release: 2%{?dist}
License: LGPLv2+ and GPLv2+
Summary: Library to parse raw trace event formats

URL: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
# If upstream does not provide tarballs, to generate:
# git clone git://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git
# cd libtraceevent
# git archive --prefix=libtraceevent-%%{version}/ -o libtraceevent-%%{version}.tar.gz %%{git_commit}
#Source0: libtraceevent-%%{version}.tar.gz
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: xmlto
BuildRequires: asciidoc

%global __provides_exclude_from ^%{_libdir}/traceevent/plugins


%description
libtraceevent is a library to parse raw trace event formats.

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Development headers of %{name}-libs

%prep
%setup -q

%build
MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
%set_build_flags
%make_build prefix=%{_prefix} libdir=%{_libdir} MANPAGE_XSL=%{MANPAGE_DOCBOOK_XSL} all doc

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} install doc-install
rm -rf %{buildroot}/%{_libdir}/libtraceevent.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/traceevent/
%{_libdir}/libtraceevent.so.%{version}
%{_libdir}/libtraceevent.so.1
%{_mandir}/man3/tep_*.3.*
%{_mandir}/man3/libtraceevent.3.*
%{_mandir}/man3/trace_seq*.3.*
%{_docdir}/%{name}-doc

%files devel
%{_includedir}/traceevent/
%{_libdir}/libtraceevent.so
%{_libdir}/pkgconfig/libtraceevent.pc

%changelog
* Thu Feb 17 2022 Zamir SUN <sztsian@gmail.com> - 1.5.0-2
- Rebuild

* Tue Feb 15 2022 Zamir SUN <sztsian@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Justin Forbes <jforbes@fedoraproject.org>
- Remove erroneus "Conflicts: perf" which broke perf.

* Mon Apr 19 2021 Zamir SUN <sztsian@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Mon Feb 08 2021 Zamir SUN <sztsian@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sat Oct 17 2020 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Oct 09 2020 Zamir SUN <sztsian@gmail.com> - 0-0.1.20201009git5dd505f
- Initial libtraceevent

