#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pika-pool
Version  : 0.1.3
Release  : 14
URL      : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Source0  : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pika-pool-python3
Requires: pika-pool-python
Requires: pika
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pika
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: pika-pool-python3

%description python
python components for the pika-pool package.


%package python3
Summary: python3 components for the pika-pool package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pika-pool package.


%prep
%setup -q -n pika-pool-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532383384
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
