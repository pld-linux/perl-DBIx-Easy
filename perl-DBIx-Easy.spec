%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Easy
Summary:	DBIx::Easy - Easy to Use DBI interface
Name:		perl-DBIx-Easy
Version:	0.15
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-DBI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Easy is an easy to use DBI interface.  Currently the Pg, mSQL,
mysql, sybase and ODBC drivers are supported.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/DBIx/Easy.pm
%{_mandir}/man[13]/*
