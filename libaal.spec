%define enable_debug 1

Name: libaal
Version: 1.0.7
Release: 1
Epoch:   1
Summary: Abstraction library for ReiserFS utilities
License: GPL
Group: Development/Libraries
URL: http://www.namesys.com/
Source: libaal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a library that provides application abstraction mechanism.
It include device abstraction, libc independence code, etc.

%package devel
Summary: Headers and static libraries for developing with libaal.
Group: Development/Libraries

%description devel
This package includes the headers and static libraries for developing
with the libaal library.

%prep
%setup -q

%build
BUILD_OPTS="--enable-libminimal"
%if %{enable_debug}
BUILD_OPTS="$BUILD_OPTS --enable-debug"
%endif

%configure \
%if %{enable_debug}
        --enable-debug \
%endif
        --enable-libminimal
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING CREDITS INSTALL NEWS README THANKS TODO
%{_libdir}/libaal-1.0.so.*
%{_libdir}/libaal-minimal.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libaal.so
%{_libdir}/libaal.*a
%{_libdir}/libaal-minimal.so
%{_libdir}/libaal-minimal.*a
%dir %{_includedir}/aal
%{_includedir}/aal/*
%{_datadir}/aclocal/libaal.m4

%changelog
* Sat Aug 14 2004 neeo <neeo@irc.pl>
- Small update for 1.0
* Fri Aug 29 2003 Yury V Umanets <umka@namesys.com>
- Different cleanups in this spec file
* Wed Aug 27 2003 David T Hollis <dhollis@davehollis.com>
- RPM package created

