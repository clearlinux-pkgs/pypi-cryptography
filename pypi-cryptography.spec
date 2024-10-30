#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: 4ea76c9
#
Name     : pypi-cryptography
Version  : 43.0.3
Release  : 183
URL      : https://files.pythonhosted.org/packages/0d/05/07b55d1fa21ac18c3a8c79f764e2514e6f6a9698f1be44994f5adf0d29db/cryptography-43.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/05/07b55d1fa21ac18c3a8c79f764e2514e6f6a9698f1be44994f5adf0d29db/cryptography-43.0.3.tar.gz
Source1  : http://localhost/cgit/vendor/pypi-cryptography/snapshot/pypi-cryptography-2024-10-30-04-18-03.tar.gz
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Unicode-DFS-2016
Requires: pypi-cryptography-license = %{version}-%{release}
Requires: pypi-cryptography-python = %{version}-%{release}
Requires: pypi-cryptography-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : pypi(cffi)
BuildRequires : pypi(maturin)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-maturin
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
%setup -q -n cryptography-43.0.3
cd %{_builddir}
tar xf %{_sourcedir}/pypi-cryptography-2024-10-30-04-18-03.tar.gz
cd %{_builddir}/cryptography-43.0.3
mkdir -p ./vendor
cp -r %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/* %{_builddir}/cryptography-43.0.3/./vendor
mkdir -p .cargo
echo '[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
' >> .cargo/config.toml

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730262269
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cryptography
cp %{_builddir}/cryptography-%{version}/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9 || :
cp %{_builddir}/cryptography-%{version}/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/asn1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/asn1_derive/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/cc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/cc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/foreign-types-shared/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/foreign-types-shared/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/bee28506691ec4e9291da8a55a450cb5304d3f5d || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/foreign-types/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/foreign-types/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/bee28506691ec4e9291da8a55a450cb5304d3f5d || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/heck/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/heck/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/memoffset/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/02bf11a87b9bbacedf2fcf4856af3b933faef82e || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/openssl-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/openssl-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/245c1d51cca7faae2e37a0e0c681efb8aa42bccf || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/openssl-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/openssl/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/ffd5a0caea8a089d58fb6acf5a4714dffb06d0dc || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pem/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pkg-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pkg-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/portable-atomic/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/portable-atomic/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-build-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-build-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-ffi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-ffi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-macros-backend/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-macros-backend/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3/pyo3-runtime/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/pyo3/pyo3-runtime/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/self_cell/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/target-lexicon/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cryptography/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-cryptography/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/vcpkg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography/f85f58f2b17e35a1c2fd852cd58e5bae165ebea9 || :
cp %{_builddir}/pypi-cryptography-2024-10-30-04-18-03/vcpkg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-cryptography/3ede8a2ceb97cd197183b1a9d7958b57cea01e14 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cryptography/02bf11a87b9bbacedf2fcf4856af3b933faef82e
/usr/share/package-licenses/pypi-cryptography/245c1d51cca7faae2e37a0e0c681efb8aa42bccf
/usr/share/package-licenses/pypi-cryptography/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-cryptography/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-cryptography/3ede8a2ceb97cd197183b1a9d7958b57cea01e14
/usr/share/package-licenses/pypi-cryptography/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-cryptography/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-cryptography/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-cryptography/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-cryptography/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pypi-cryptography/62130e917677e059de5fb38e7bfdd72f299bb1f8
/usr/share/package-licenses/pypi-cryptography/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/pypi-cryptography/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-cryptography/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-cryptography/959ce149b1615b8bff3437f59282396756987859
/usr/share/package-licenses/pypi-cryptography/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-cryptography/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/pypi-cryptography/b9b8e747d9af5285e3cf6852d84ec355b39c70e8
/usr/share/package-licenses/pypi-cryptography/bee28506691ec4e9291da8a55a450cb5304d3f5d
/usr/share/package-licenses/pypi-cryptography/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/pypi-cryptography/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/pypi-cryptography/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-cryptography/f85f58f2b17e35a1c2fd852cd58e5bae165ebea9
/usr/share/package-licenses/pypi-cryptography/ffd5a0caea8a089d58fb6acf5a4714dffb06d0dc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
