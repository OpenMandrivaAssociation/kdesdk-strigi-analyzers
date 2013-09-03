Summary:	Strigi analyzers for diff, po, ts and xlf files
Name:		kdesdk-strigi-analyzers
Version:	4.11.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libstreamanalyzer)
Conflicts:	kdesdk4-strigi-analyzer < 1:4.11.0
Obsoletes:	kdesdk4-strigi-analyzer < 1:4.11.0
Conflicts:	lokalize < 1:4.11.0

%description
Strigi analyzers for diff, po, ts and xlf files.

%files
%{_kde_libdir}/strigi/strigila_diff.so
%{_kde_libdir}/strigi/strigila_po.so
%{_kde_libdir}/strigi/strigita_ts.so
%{_kde_libdir}/strigi/strigita_xlf.so
%{_kde_datadir}/strigi/fieldproperties/strigi_translation.fieldproperties

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0