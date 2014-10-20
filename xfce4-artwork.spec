%define		snap		20110420
Summary:	Additional artwork for the Xfce
Summary(pl.UTF-8):	Dodatkowe ozdobniki dla Xfce
Name:		xfce4-artwork
Version:	0.1.1a
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.debian.org/debian/pool/main/x/xfce4-artwork/%{name}_%{version}~git+%{snap}.orig.tar.gz
# Source0-md5:	b7612ee950fcf052e5acfacd0fda729f
URL:		http://xfce-goodies.berlios.de/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		bgdir	%{_datadir}/backgrounds/xfce

%description
Additional artwork (backgrounds...) for the Xfce desktop environment.

%description -l pl.UTF-8
Dodatkowe ozdobniki (tapety...) dla środowiska Xfce.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	backdropsdir=$RPM_BUILD_ROOT%{bgdir}
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%{bgdir}/*
