Name:		jansson
Version:	2.0
Release:	1%{?dist}
Summary:	Javascript Object Notation parsing library

Group:		System Environment/Libraries
License:	2-clause BSD
URL:		http://www.digip.org/jansson/doc/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root


%description
A JSON parser.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT
%package devel
Summary: Development files for %{name}

%description devel
Development files for jansson.



%files
%defattr(-,root,root,-)
%doc README.rst 
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*



%changelog
