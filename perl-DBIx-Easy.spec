%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-Easy perl module
Summary(pl):	Modu� perla DBIx-Easy
Name:		perl-DBIx-Easy
Version:	0.10
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-Easy-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-CSV_XS
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx-Easy perl module.

%description -l pl
Modu� perla DBIx-Easy.

%prep
%setup -q -n DBIx-Easy-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/DBIx/Easy.pm
%{_mandir}/man[13]/*
