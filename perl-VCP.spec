#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	VCP
Summary:	Data::VCP - Versioned Copy, copying hierarchies of versioned files
Summary(pl):	Data::VCP - wersjonowane kopie - kopiowanie hierarchii wersjonowanych plików
Name:		perl-VCP
Version:	0.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{pnam}-%{version}.tar.gz
# Source0-md5:	4055bc73d33ebfb27e371d28ced8e8de
BuildRequires:	perl-BFD
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-PodToHTML
BuildRequires:	perl-Text-Table
BuildRequires:	perl-XML-AutoWriter
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(mkss)'

%description
Versioned Copy, copying hierarchies of versioned files.

%description -l pl
Wersjonowane kopie - kopiowanie hierarchii wersjonowanych plików.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE*
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/RevML
%{perl_vendorlib}/VCP
%{perl_vendorlib}/VCP.pm
%{_mandir}/man[13]/*
