#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pika-pool
Version  : 0.1.3
Release  : 8
URL      : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Source0  : https://github.com/bninja/pika-pool/archive/v0.1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pika-pool-python
Requires: pika
BuildRequires : pbr
BuildRequires : pika
BuildRequires : pip
BuildRequires : python-dev
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

%description python
python components for the pika-pool package.


%prep
%setup -q -n pika-pool-0.1.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487904912
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487904912
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
