#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cryptography
Version  : 37.0.4
Release  : 162
URL      : https://files.pythonhosted.org/packages/89/d9/5fcd312d5cce0b4d7ee8b551a0ea99e4ea9db0fdbf6dd455a19042e3370b/cryptography-37.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/d9/5fcd312d5cce0b4d7ee8b551a0ea99e4ea9db0fdbf6dd455a19042e3370b/cryptography-37.0.4.tar.gz
Source1  : http://localhost/cgit/projects/cryptography-vendor/snapshot/cryptography-vendor-37.0.2.tar.xz
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0
Requires: pypi-cryptography-filemap = %{version}-%{release}
Requires: pypi-cryptography-lib = %{version}-%{release}
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

%description
pyca/cryptography
=================
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.org/project/cryptography/
:alt: Latest Version

%package filemap
Summary: filemap components for the pypi-cryptography package.
Group: Default

%description filemap
filemap components for the pypi-cryptography package.


%package lib
Summary: lib components for the pypi-cryptography package.
Group: Libraries
Requires: pypi-cryptography-license = %{version}-%{release}
Requires: pypi-cryptography-filemap = %{version}-%{release}

%description lib
lib components for the pypi-cryptography package.


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
Requires: pypi-cryptography-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(cryptography)
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the pypi-cryptography package.


%prep
%setup -q -n cryptography-37.0.4
cd %{_builddir}
tar xf %{_sourcedir}/cryptography-vendor-37.0.2.tar.xz
cd %{_builddir}/cryptography-37.0.4
mkdir -p ./
cp -r %{_builddir}/cryptography-vendor-37.0.2/* %{_builddir}/cryptography-37.0.4/./
pushd ..
cp -a cryptography-37.0.4 buildavx2
popd

%build
## build_prepend content
mkdir -p $HOME/.cargo
cat > $HOME/.cargo/config.toml << "EOF"
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
ln -s $PWD/vendor $HOME/vendor
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657054166
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cryptography
cp %{_builddir}/cryptography-37.0.4/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography-37.0.4/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
cp %{_builddir}/cryptography-37.0.4/LICENSE.PSF %{buildroot}/usr/share/package-licenses/pypi-cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/aliasable/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5f2da41389ce5873a46945bc1b75454acfd75cf6
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/asn1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/asn1_derive/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/chrono/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cryptography/c145b1a607ecf06aed81f1d04a65c2e43dffdc63
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/indoc-impl/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/indoc-impl/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/instant/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/037192733999bccd7ed8d75123b7ec09feb4a12d
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/lazy_static/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/lazy_static/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/num-integer/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/num-integer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/num-traits/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/num-traits/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/paste-impl/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/paste-impl/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/paste/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/paste/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/pem/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-error-attr/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/a88eaffea57a51eedb5291e0d55a959df7659458
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-error-attr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-error/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/197cb40dc96ded1e036d13ef67fdc7a758ca1388
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-error/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-hack/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro-hack/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/594599b254cfdf4e8e7a570660d3f7861362acaf
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/pyo3-build-config/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/pyo3-macros-backend/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/pyo3-macros/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/pyo3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/a00165152c82ea55b9fc254890dc8860c25e3bb6
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/f498d95a48889a0b1432e420e6754881eff1d593
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/c61640f6c218caf86d1b8072e09668a8362dba04
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/stable_deref_trait/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/stable_deref_trait/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/f81793ddf50f460d6111fcbc799cab1a804aa000
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/unicode-xid/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-cryptography/5ed53061419caf64f84d064f3641392a2a10fa7f
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/unicode-xid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/unicode-xid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/60c3522081bf15d7ac1d4c5a63de425ef253e87a
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/cfcb552ef0afbe7ccb4128891c0de00685988a4b
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cryptography-vendor-37.0.2/vendor/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/2243f7a86daaa727d34d92e987a741036f288464
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-cryptography

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cryptography/037192733999bccd7ed8d75123b7ec09feb4a12d
/usr/share/package-licenses/pypi-cryptography/197cb40dc96ded1e036d13ef67fdc7a758ca1388
/usr/share/package-licenses/pypi-cryptography/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/pypi-cryptography/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84
/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-cryptography/594599b254cfdf4e8e7a570660d3f7861362acaf
/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-cryptography/5ed53061419caf64f84d064f3641392a2a10fa7f
/usr/share/package-licenses/pypi-cryptography/5f2da41389ce5873a46945bc1b75454acfd75cf6
/usr/share/package-licenses/pypi-cryptography/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8
/usr/share/package-licenses/pypi-cryptography/655a437377cc2780990746fe2492fa16764df083
/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-cryptography/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/pypi-cryptography/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-cryptography/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-cryptography/a88eaffea57a51eedb5291e0d55a959df7659458
/usr/share/package-licenses/pypi-cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8
/usr/share/package-licenses/pypi-cryptography/c145b1a607ecf06aed81f1d04a65c2e43dffdc63
/usr/share/package-licenses/pypi-cryptography/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-cryptography/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/pypi-cryptography/d17529544f8be8ea552caaa5258defb240be625b
/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/pypi-cryptography/f498d95a48889a0b1432e420e6754881eff1d593
/usr/share/package-licenses/pypi-cryptography/f81793ddf50f460d6111fcbc799cab1a804aa000

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
