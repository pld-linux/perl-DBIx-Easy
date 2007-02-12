%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	Easy
Summary:	DBIx::Easy - easy to use DBI interface
Summary(pl.UTF-8):   DBIx::Easy - łatwy w użyciu interfejs DBI
Name:		perl-DBIx-Easy
Version:	1.40
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	854234349c30a05d44cdb89c56cd8c43
URL:		http://search.cpan.org/dist/DBIx-Easy/
BuildRequires:	perl-DBI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Easy is an easy to use DBI interface. Currently the Pg, mSQL,
MySQL, sybase and ODBC drivers are supported.

%description -l pl.UTF-8
DBIx::Easy to łatwy w użyciu interfejs DBI. Aktualnie obsługuje
sterowniki Pg, mSQL, MySQL, sybase i ODBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/Easy.pm
%{perl_vendorlib}/DBIx/Easy/MySQL.pm
%{perl_vendorlib}/DBIx/Easy/SQLite.pm
%dir %{perl_vendorlib}/auto/DBIx
%dir %{perl_vendorlib}/auto/DBIx/Easy
%dir %{perl_vendorlib}/auto/DBIx/Easy/MySQL
%{perl_vendorlib}/auto/DBIx/Easy/MySQL/autosplit.ix
%dir %{perl_vendorlib}/auto/DBIx/Easy/SQLite
%{perl_vendorlib}/auto/DBIx/Easy/SQLite/autosplit.ix
%{_mandir}/man[13]/*
