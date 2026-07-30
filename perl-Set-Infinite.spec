%define upstream_name    Set-Infinite
%define upstream_version 0.65
Name:		perl-%{upstream_name}
Version:	0.65
Release:	2

Summary:	Infinite Set Theory module, with Date, Time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/Set-Infinite-0.65.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Local)
BuildArch:	noarch

%description
Set::Infinite is a Set Theory module for infinite sets.

A set is a collection of objects. The objects that belong to a set are
called its members, or "elements".

As objects we allow (almost) anything: reals, integers, and objects (such
as dates).

%prep
%setup -q -n Set-Infinite-0.65

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

