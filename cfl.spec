Summary:	Configuration File Library
Summary(pl):	Biblioteka plików konfiguracyjnych
Name:		cfl
Version:	0.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://freesoftware.fsf.org/download/cfl/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://www.freesoftware.fsf.org/cfl/
BuildRequires:	gdsl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libcfl

%description
The Configuration File Library (CFL) is a collection of routines for
manipulating configuration files. CFL provides a modern Applications
Programming Interface (API) for C programmers, while allowing wrappers
to be written for very high level languages.

%description -l pl
Biblioteka plików konfiguracyjnych (CFL: Configuration File Library)
jest zestawem funkcji do obróbki plików konfiguracyjnych. CFL
dostarcza nowoczesne API dla programistów C, pozwalaj±c na pisanie
wrapperów na bardzo wysokich poziomach jêzyków.

%package devel
Summary:	Header files and development documentation for Configuration File Library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki plików konfiguracyjnych
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libcfl-devel

%description devel
Header files and development documentation for Configuration File
Library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki plików konfiguracyjnych.

%package static
Summary:	Static Log Writer Library
Summary(pl):	Statyczna biblioteka plików konfiguracyjnych
Group:		Development/Libraries
Obsoletes:	libcfl-static

%description static
Static Log Writer Library.

%description static -l pl
Statyczna biblioteka plików konfiguracyjnych.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc src/example.c doc/ref/html/{*.html,*.gif}
%attr(755,root,root) %{_libdir}/*.so.?
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*.h

%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
