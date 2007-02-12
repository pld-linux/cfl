Summary:	Configuration File Library
Summary(pl.UTF-8):   Biblioteka plików konfiguracyjnych
Name:		cfl
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.gna.org/cfl/%{name}-%{version}.tar.gz
# Source0-md5:	2db9b1023f29274057368ce73959639d
Patch0:		%{name}-ac.patch
URL:		http://home.gna.org/cfl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdsl-devel
BuildRequires:	libtool
Obsoletes:	libcfl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Configuration File Library (CFL) is a collection of routines for
manipulating configuration files. CFL provides a modern Applications
Programming Interface (API) for C programmers, while allowing wrappers
to be written for very high level languages.

%description -l pl.UTF-8
Biblioteka plików konfiguracyjnych (CFL: Configuration File Library)
jest zestawem funkcji do obróbki plików konfiguracyjnych. CFL
dostarcza nowoczesne API dla programistów C, pozwalając na pisanie
wrapperów na bardzo wysokich poziomach języków.

%package devel
Summary:	Header files and development documentation for Configuration File Library
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do biblioteki plików konfiguracyjnych
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libcfl-devel

%description devel
Header files and development documentation for Configuration File
Library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki plików konfiguracyjnych.

%package static
Summary:	Static Log Writer Library
Summary(pl.UTF-8):   Statyczna biblioteka plików konfiguracyjnych
Group:		Development/Libraries
Obsoletes:	libcfl-static

%description static
Static Log Writer Library.

%description static -l pl.UTF-8
Statyczna biblioteka plików konfiguracyjnych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install src/example.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/ref/html/{*.html,*.gif}
%attr(755,root,root) %{_libdir}/*.so
%{_examplesdir}/%{name}-%{version}
%{_includedir}/*.h
%{_libdir}/*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
