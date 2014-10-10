%define upstream_name    Set-Infinite
%define upstream_version 0.65

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Infinite Set Theory module, with Date, Time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.650.0-2mdv2011.0
+ Revision: 655217
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.650.0-1mdv2011.0
+ Revision: 542920
- import perl-Set-Infinite


* Thu May 06 2010 cpan2dist 0.65-1mdv
- initial mdv release, generated with cpan2dist
