#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Manifest
Version  : 2.023
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Test-Manifest-2.023.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Test-Manifest-2.023.tar.gz
Summary  : 'interact with a t/test_manifest file'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Test-Manifest-license = %{version}-%{release}
Requires: perl-Test-Manifest-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Test-Manifest package.
Group: Development
Provides: perl-Test-Manifest-devel = %{version}-%{release}
Requires: perl-Test-Manifest = %{version}-%{release}

%description dev
dev components for the perl-Test-Manifest package.


%package license
Summary: license components for the perl-Test-Manifest package.
Group: Default

%description license
license components for the perl-Test-Manifest package.


%package perl
Summary: perl components for the perl-Test-Manifest package.
Group: Default
Requires: perl-Test-Manifest = %{version}-%{release}

%description perl
perl components for the perl-Test-Manifest package.


%prep
%setup -q -n Test-Manifest-2.023
cd %{_builddir}/Test-Manifest-2.023

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Manifest
cp %{_builddir}/Test-Manifest-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Manifest/22bc6b9310295913e198979ee064ecc65120b04d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Manifest.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Manifest/22bc6b9310295913e198979ee064ecc65120b04d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
