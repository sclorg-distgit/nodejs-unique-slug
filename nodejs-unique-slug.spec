%{?scl:%scl_package nodejs-unique-slug}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename unique-slug
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-unique-slug
Version:	2.0.0
Release:	4%{?dist}
Summary:	Generate a unique character string suitable for use in files and URLs

License:	ISC
URL:		https://github.com/iarna/unique-slug.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	LICENSE-ISC.txt
# No upstream license file, but one has been requested
# at https://github.com/npm/unique-slug/issues/2

Patch0:		nodejs-unique-slug_fix_tests.patch
# the version of npm(tap) in Fedora is *very* old, so we have to patch the
# syntax to fit the old version of tap.  If tap gets updated, we can remove
# this patch.

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
BuildRequires:	%{?scl_prefix}npm(imurmurhash)
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Generate a unique character string suitable for use in files and URLs.

%prep
%setup -q -n package
cp -p %{SOURCE1} .
%patch0 -p1

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{_bindir}/tap --coverage test
#%else
#%{_bindir}/echo "Tests disabled..."
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-ISC.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Built for RHSCL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- Initial packaging
