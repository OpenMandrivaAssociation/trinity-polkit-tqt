%bcond clang 1

# TDE variables
%define tde_pkg polkit-tqt

%define libname %mklibname %{tde_pkg}
%define devname %mklibname %{tde_pkg} -d

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	PolicyKit-tqt library
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/dependencies/%{tarball_name}-%{version}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tde-cmake >= %{version}
BuildRequires:	pkgconfig(dbus-1-tqt)
BuildRequires:	pkgconfig(tqt)
BuildRequires:  tqt3-dev-tools

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	gettext

BuildRequires:	pkgconfig(polkit-agent-1)

%description
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains the files necessary for running applications that use
the libpolkit-tqt library.

##########

%package -n %{libname}0
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++

%description -n %{libname}0
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains the files necessary for running applications that use
the libpolkit-tqt library.

%files -n %{libname}0
%defattr(-,root,root,-)
%{_libdir}/libpolkit-tqt-agent.so.0
%{_libdir}/libpolkit-tqt-agent.so.0.0.0
%{_libdir}/libpolkit-tqt-core.so.0
%{_libdir}/libpolkit-tqt-core.so.0.0.0
%{_libdir}/libpolkit-tqt-gui.so.0
%{_libdir}/libpolkit-tqt-gui.so.0.0.0

##########

%package -n %{devname}
Summary:	PolicyKit-tqt development files
Group:		Development/Libraries/C and C++

Requires:	%{libname}0 = %{EVRD}

%description -n %{devname}
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.
.
This package contains the development libraries and headers.

%files -n %{devname}
%defattr(-,root,root,-)
%{_includedir}/polkit-tqt/
%{_libdir}/cmake/polkit-tqt.cmake
%{_libdir}/libpolkit-tqt-agent.so
%{_libdir}/libpolkit-tqt-core.so
%{_libdir}/libpolkit-tqt-gui.so
%{_libdir}/pkgconfig/polkit-tqt-agent.pc
%{_libdir}/pkgconfig/polkit-tqt-core.pc
%{_libdir}/pkgconfig/polkit-tqt-gui.pc
%{_libdir}/pkgconfig/polkit-tqt.pc

##########

%package -n %{libname}-examples
Summary:	Polkit-tqt Documentation
Group:		Development/Libraries/C and C++
Provides:	%{libname}-doc = %{EVRD}
Requires:	%{libname}0 = %{EVRD}
Requires:	trinity-filesystem >= %{version}

%description -n %{libname}-examples
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains example files and applications.

%files -n %{libname}-examples
%defattr(-,root,root,-)
%{_sysconfdir}/dbus-1/system.d/org.tqt.policykit.examples.conf
%{_bindir}/polkit-tqt-agent-example
%{_bindir}/polkit-tqt-example
%{_bindir}/polkit-tqt-example-helper
%dir %{_datadir}/apps/
%{_datadir}/apps/polkit-tqt/
%{_datadir}/dbus-1/system-services/org.tqt.policykit.examples.service
%{_datadir}/polkit-1/actions/org.tqt.policykit.examples.policy


%conf -p
unset QTDIR QTINC QTLIB


%install -a
# Unwanted files
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-agent.la
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-core.la
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-gui.la

