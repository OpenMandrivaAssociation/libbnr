%define	major 2
%define libname %mklibname bnr %{major}
%define develname %mklibname bnr -d

Summary:	Bayesian Noise Reduction Library
Name:		libbnr
Version:	2.0.3
Release:	9
Group:		System/Libraries
License:	GPL
URL:		https://bnr.nuclearelephant.com/
Source0:	http://dspam.nuclearelephant.com/sources/%{name}-%{version}.tar.bz2
BuildRequires:	automake
BuildRequires:	autoconf2.5
BuildRequires:	libtool

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

%package -n	%{develname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname bnr 2 -d}

%description -n	%{develname}
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
#libtoolize --copy --force && aclocal && autoconf --force && autoheader && automake

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std


%files -n %{libname}
%doc README
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-7mdv2011.0
+ Revision: 627784
- don't force the usage of automake1.7

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-6mdv2011.0
+ Revision: 620083
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.3-5mdv2010.0
+ Revision: 429717
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3-4mdv2009.0
+ Revision: 248411
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0.3-2mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-2mdv2008.0
+ Revision: 83754
- new devel naming


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-1mdv2007.0
+ Revision: 93731
- Import libbnr

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-1mdk
- 2.0.3

* Wed Dec 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.0-1mdk
- initial mandrake package

