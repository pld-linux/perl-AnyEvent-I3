Summary:	AnyEvent::I3 - Communicate with the i3 window manager
Name:		perl-AnyEvent-I3
Version:	0.17
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-I3-%{version}.tar.gz
# Source0-md5:	907b6ed7fe6bea5914b878cdd73aba3f
URL:		http://search.cpan.org/dist/AnyEvent-I3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module connects to the i3 window manager using the UNIX socket
based IPC interface it provides (if enabled in the configuration
file). You can then subscribe to events or send messages and receive
their replies.

%prep
%setup -q -n AnyEvent-I3-%{version}

%build
echo "n" | \
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
%{perl_vendorlib}/AnyEvent/I3.pm
%{_mandir}/man3/AnyEvent::I3*.3pm*
