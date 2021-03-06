# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate hmac

Name:           rust-%{crate}
Version:        0.7.1
Release:        2%{?dist}
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/hmac
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Generic implementation of Hash-based Message Authentication Code (HMAC).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 17:43:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:16:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-2
- Regenerate

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Initial package
