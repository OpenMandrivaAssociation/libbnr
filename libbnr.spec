%define	major 2
%define libname	%mklibname bnr %{major}

Summary:	Bayesian Noise Reduction Library
Name:		libbnr
Version:	2.0.3
Release:	%mkrel 1
Group:		System/Libraries
License:	GPL
URL:		http://bnr.nuclearelephant.com/
Source0:	http://dspam.nuclearelephant.com/sources/%{name}-%{version}.tar.bz2
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libbnr is an implementation of the Bayesian Noise Reduction (BNR)
algorithm. All samples of text contain some degree of noise (data
which is either intentionally or unintentionally irrelevant to
accurate statistical analysis of the sample where removal of the
data would result in a cleaner analysis). The Bayesian noise
reduction algorithm provides a means of cleaner machine learning
by providing more useful data, which ultimately leads to better
sample analysis. With the noisy data removed from the sample, what
is left is only data relevant to the classification. libbnr can be
linked in with your classifier and called using the standard C
interface. 

%package -n	%{libname}
Summary:	Bayesian Noise Reduction Library
Group:          System/Libraries

%description -n	%{libname}
libbnr is an implementation of the Bayesian Noise Reduction (BNR)
algorithm. All samples of text contain some degree of noise (data
which is either intentionally or unintentionally irrelevant to
accurate statistical analysis of the sample where removal of the
data would result in a cleaner analysis). The Bayesian noise
reduction algorithm provides a means of cleaner machine learning
by providing more useful data, which ultimately leads to better
sample analysis. With the noisy data removed from the sample, what
is left is only data relevant to the classification. libbnr can be
linked in with your classifier and called using the standard C
interface. 

%package -n	%{libname}-devel
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
libbnr is an implementation of the Bayesian Noise Reduction (BNR)
algorithm. All samples of text contain some degree of noise (data
which is either intentionally or unintentionally irrelevant to
accurate statistical analysis of the sample where removal of the
data would result in a cleaner analysis). The Bayesian noise
reduction algorithm provides a means of cleaner machine learning
by providing more useful data, which ultimately leads to better
sample analysis. With the noisy data removed from the sample, what
is left is only data relevant to the classification. libbnr can be
linked in with your classifier and called using the standard C
interface. 

This package contains development library and header files for the
%{name} library.

%prep

%setup -q -n %{name}-%{version}

%build
#export WANT_AUTOCONF_2_5=1
#rm -f configure
#libtoolize --copy --force && aclocal-1.7 && autoconf --force && autoheader && automake-1.7

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


