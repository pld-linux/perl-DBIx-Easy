%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Easy
Summary:	DBIx::Easy - easy to use DBI interface
Summary(pl):	DBIx::Easy - ³atwy w u¿yciu interfejs DBI
Name:		perl-DBIx-Easy
Version:	0.15
Release:	4
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	438be47d8dfda8a559cfeeaeaa3a31ea
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-DBI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	rpm-perlprov >= 4.1-13
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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/DBIx/Easy.pm
%{_mandir}/man[13]/*
