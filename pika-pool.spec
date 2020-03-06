#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pika-pool
Version  : 0.1.3
Release  : 19
URL      : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Source0  : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Summary  : Pools for pikas.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pika-pool-python = %{version}-%{release}
Requires: pika-pool-python3 = %{version}-%{release}
Requires: pika
BuildRequires : buildreq-distutils3
BuildRequires : pika

%description
=========
pika-pool
=========
.. image:: https://travis-ci.org/bninja/pika-pool.png
:target: https://travis-ci.org/bninja/pika-pool

.. image:: https://coveralls.io/repos/bninja/pika-pool/badge.png?branch=master
:target: https://coveralls.io/r/bninja/pika-pool?branch=master

%package python
Summary: python components for the pika-pool package.
Group: Default
Requires: pika-pool-python3 = %{version}-%{release}

%description python
python components for the pika-pool package.


%package python3
Summary: python3 components for the pika-pool package.
Group: Default
Requires: python3-core
Provides: pypi(pika_pool)
Requires: pypi(pika)

%description python3
python3 components for the pika-pool package.


%prep
%setup -q -n pika-pool-0.1.3
cd %{_builddir}/pika-pool-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583538975
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
