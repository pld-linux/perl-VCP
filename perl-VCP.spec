#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#			  [why it was disabled instead of fixing?]
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	VCP
Summary:	Data::VCP - Versioned Copy, copying hierarchies of versioned files
Summary(pl.UTF-8):	Data::VCP - wersjonowane kopie - kopiowanie hierarchii wersjonowanych plików
Name:		perl-VCP
%define _snap	20050110
%define	_ver	0.9
Version:	%{_ver}_%{_snap}
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/A/AU/AUTRIJUS/VCP-autrijus-snapshot-%{_ver}-%{_snap}.tar.gz
# Source0-md5:	c01249d810904f5b4f6080979673a514
URL:		http://search.cpan.org/~autrijus/VCP-autrijus-snapshot/
BuildRequires:	perl-BFD
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-PodToHTML
BuildRequires:	perl-Regexp-Shellish >= 0.93
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-Text-Table
BuildRequires:	perl-XML-AutoWriter
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(mkss)' 'perl(VCP::.*)' 'perl(RevML::.*)'

%description
Versioned Copy, copying hierarchies of versioned files.

%description -l pl.UTF-8
Wersjonowane kopie - kopiowanie hierarchii wersjonowanych plików.

%prep
%setup -q -n VCP-autrijus-snapshot-%{_ver}-%{_snap}

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
