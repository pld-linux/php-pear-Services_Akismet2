%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Akismet2
%define		_status		alpha
%define		_pearname	Services_Akismet2
Summary:	%{_pearname} - PHP client for the Akismet REST API
Summary(pl.UTF-8):	%{_pearname} - Klient PHP do API REST Akismet
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	898089999dcf97c1ff1e2c13a5c3a2f0
URL:		http://pear.php.net/package/Services_Akismet2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request2 >= 0.1.0
Requires:	php-pear-PEAR >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object-oriented interface to the Akismet REST
API. The Akismet API is used to detect and to filter spam comments
posted on weblogs.

There are several anti-spam service providers that use the Akismet
API. To use the API, you will need an API key from such a provider.
Example providers include Wordpress (http://wordpress.com) and TypePad
(http://antispam.typepad.com).

Most services are free for personal or low-volume use, and offer
licensing for commercial or high-volume applications.

This package is derived from the miPHP Akismet class written by Bret
Kuhns for use in PHP 4. This package requires PHP 5.2.1.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza zorientowanego obiektowo interfejsu do API REST
Akismet, wykorzystywanego do wykrywania i filtorwania spamów w
komentarzach do wpisów na blogach. Chociaż wykorzystanie API jest
możliwe nie tylko z blogiem wordpress, do korzystania z tego pakietu
konieczne będzie pobranie klucza Wordpress API ze strony
http://wordpress.com/api-keys/ .

Akismet jest darmowe dla prywatnego użytku, licencję można nabyć dla
serwisów komercyjnych lub o dużym natężeniu ruchu.

Pakiet ten jest wzorowany na napisanej dla PHP 4 klasie miPHP Akismet,
której autorem jest Bret Kuhns.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Akismet2
%{php_pear_dir}/Services/Akismet2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Akismet2
