Summary:	Additional artwork for the XFce.
Summary(pl):	Dodatkowe ozdobniki dla XFce
Name:		xfce4-artwork
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	7b5d96c987a61b1a847b2010b1947244
URL:		http://xfce-goodies.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional artwork (backgrounds...) for the XFce desktop environment.

%description -l pl
Dodatkowe ozdobniki (tapety...) dla środowiska XFce.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%{_datadir}/xfce4/backdrops/*
