%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Easy
Summary:	DBIx::Easy - Easy to Use DBI interface
Summary(pl):	DBIx::Easy - ³atwy w u¿yciu interfejs DBI
Name:		perl-DBIx-Easy
Version:	0.15
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-DBI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Easy is an easy to use DBI interface.  Currently the Pg, mSQL,
mysql, sybase and ODBC drivers are supported.

%description -l pl
DBIx::Easy to ³atwy w u¿yciu interfejs DBI. Aktualnie obs³uguje
sterowniki Pg, mSQL, mysql, sybase i ODBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
