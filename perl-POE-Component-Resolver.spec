%define upstream_name    POE-Component-Resolver
%define upstream_version 0.912

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A non-blocking getaddrinfo() resolver
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(POE)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Socket::GetAddrInfo)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::Resolver performs Socket::GetAddrInfo::getaddrinfo() calls
in subprocesses where they're permitted to block as long as necessary.

By default it will run eight subprocesses and prefer address families in
whatever order Socket::GetAddrInfo returns them. These defaults can be
overridden with constructor parameters.

PUBLIC METHODS
    new
        Create a new resolver. Returns an object that must be held and used
        to make requests. See the synopsis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


