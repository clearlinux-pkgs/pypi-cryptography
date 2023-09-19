#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : pypi-cryptography
Version  : 38.0.4
Release  : 173
URL      : https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz
Source1  : http://localhost/cgit/projects/cryptography-vendor/snapshot/cryptography-vendor-38.0.1.tar.xz
Source2  : https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz.asc
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0 Unicode-DFS-2016
Requires: pypi-cryptography-license = %{version}-%{release}
Requires: pypi-cryptography-python = %{version}-%{release}
Requires: pypi-cryptography-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pypi(cffi)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_rust)
BuildRequires : pypi(wheel)
BuildRequires : rustc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pyca/cryptography
=================
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.org/project/cryptography/
:alt: Latest Version

%package license
Summary: license components for the pypi-cryptography package.
Group: Default

%description license
license components for the pypi-cryptography package.


%package python
Summary: python components for the pypi-cryptography package.
Group: Default
Requires: pypi-cryptography-python3 = %{version}-%{release}

%description python
python components for the pypi-cryptography package.


%package python3
Summary: python3 components for the pypi-cryptography package.
Group: Default
Requires: python3-core
Provides: pypi(cryptography)
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the pypi-cryptography package.


%prep
%setup -q -n cryptography-38.0.4
cd %{_builddir}
tar xf %{_sourcedir}/cryptography-vendor-38.0.1.tar.xz
cd %{_builddir}/cryptography-38.0.4
mkdir -p ./
cp -r %{_builddir}/cryptography-vendor-38.0.1/* %{_builddir}/cryptography-38.0.4/./
pushd ..
cp -a cryptography-38.0.4 buildavx2
popd

%build
## build_prepend_once content
mkdir -p $HOME/.cargo
cat > $HOME/.cargo/config.toml << "EOF"
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
ln -s $PWD/vendor $HOME/vendor
## build_prepend_once end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695149528
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cryptography
cp %{_builddir}/cryptography-%{version}/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9 || :
cp %{_builddir}/cryptography-%{version}/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/cryptography-%{version}/LICENSE.PSF %{buildroot}/usr/share/package-licenses/pypi-cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/aliasable/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5f2da41389ce5873a46945bc1b75454acfd75cf6 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/android_system_properties/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/a8ab3e6caa5e7af0ec9235d5db800ace830c0a38 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/android_system_properties/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ac0bf7546a377351144d930c5e31eff058fe4e8f || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/asn1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/asn1_derive/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/bumpalo/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/bumpalo/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/0a1e89ac22450cb0311baa2613bc21b7131b321f || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/chrono/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cryptography/c145b1a607ecf06aed81f1d04a65c2e43dffdc63 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/core-foundation-sys/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/core-foundation-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/6c2945f449081ab19640fb7c70a081a1a4559399 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/iana-time-zone/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/ff44b187892fcf1cd15a3ca61b498041b28afecc || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/iana-time-zone/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/d3f4001d9de83a122956c9195d73e2507bf6c533 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/indoc-impl/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/indoc-impl/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/instant/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/037192733999bccd7ed8d75123b7ec09feb4a12d || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/js-sys/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/js-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/log/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/aca374a3362a76702c50bd4e7d590a57f8834fc7 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/log/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/num-integer/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/num-integer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/num-traits/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/num-traits/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/ouroboros/LICENSE_APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/97217ef49a087b476f6a7a16bb79c743492786e3 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/ouroboros/LICENSE_MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/5f0a6236f4e77988d403a2ff7465671427fa267f || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/ouroboros_macro/LICENSE_APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/97217ef49a087b476f6a7a16bb79c743492786e3 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/ouroboros_macro/LICENSE_MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/5f0a6236f4e77988d403a2ff7465671427fa267f || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/paste-impl/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/paste-impl/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/paste/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/paste/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/pem/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-error-attr/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/a88eaffea57a51eedb5291e0d55a959df7659458 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-error-attr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-error/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/197cb40dc96ded1e036d13ef67fdc7a758ca1388 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-error/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-hack/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro-hack/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/594599b254cfdf4e8e7a570660d3f7861362acaf || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/pyo3-build-config/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/pyo3-macros-backend/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/pyo3-macros/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/pyo3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/a00165152c82ea55b9fc254890dc8860c25e3bb6 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/f498d95a48889a0b1432e420e6754881eff1d593 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-cryptography/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/cfcb552ef0afbe7ccb4128891c0de00685988a4b || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-backend/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-backend/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-macro-support/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-macro-support/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-macro/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-macro/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-shared/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen-shared/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/wasm-bindgen/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cryptography-vendor-38.0.1/vendor/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/2243f7a86daaa727d34d92e987a741036f288464 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cryptography/037192733999bccd7ed8d75123b7ec09feb4a12d
/usr/share/package-licenses/pypi-cryptography/0a1e89ac22450cb0311baa2613bc21b7131b321f
/usr/share/package-licenses/pypi-cryptography/197cb40dc96ded1e036d13ef67fdc7a758ca1388
/usr/share/package-licenses/pypi-cryptography/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-cryptography/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-cryptography/594599b254cfdf4e8e7a570660d3f7861362acaf
/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-cryptography/5f0a6236f4e77988d403a2ff7465671427fa267f
/usr/share/package-licenses/pypi-cryptography/5f2da41389ce5873a46945bc1b75454acfd75cf6
/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8
/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083
/usr/share/package-licenses/pypi-cryptography/6c2945f449081ab19640fb7c70a081a1a4559399
/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-cryptography/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/pypi-cryptography/97217ef49a087b476f6a7a16bb79c743492786e3
/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-cryptography/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-cryptography/a88eaffea57a51eedb5291e0d55a959df7659458
/usr/share/package-licenses/pypi-cryptography/a8ab3e6caa5e7af0ec9235d5db800ace830c0a38
/usr/share/package-licenses/pypi-cryptography/ac0bf7546a377351144d930c5e31eff058fe4e8f
/usr/share/package-licenses/pypi-cryptography/aca374a3362a76702c50bd4e7d590a57f8834fc7
/usr/share/package-licenses/pypi-cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8
/usr/share/package-licenses/pypi-cryptography/c145b1a607ecf06aed81f1d04a65c2e43dffdc63
/usr/share/package-licenses/pypi-cryptography/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-cryptography/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b
/usr/share/package-licenses/pypi-cryptography/d3f4001d9de83a122956c9195d73e2507bf6c533
/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/pypi-cryptography/f498d95a48889a0b1432e420e6754881eff1d593
/usr/share/package-licenses/pypi-cryptography/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8
/usr/share/package-licenses/pypi-cryptography/ff44b187892fcf1cd15a3ca61b498041b28afecc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
