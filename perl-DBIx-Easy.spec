%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-Easy perl module
Summary(pl):	Modu� perla DBIx-Easy
Name:		perl-DBIx-Easy
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-Easy-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Term-ReadKey
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
DBIx-Easy perl module

%description -l pl
Modu� perla DBIx-Easy

%prep
%setup -q -n DBIx-Easy-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBIx/Easy
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/DBIx/Easy.pm
%{perl_sitearch}/auto/DBIx/Easy

%{_mandir}/man[13]/*