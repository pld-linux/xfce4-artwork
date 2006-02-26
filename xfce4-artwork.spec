Summary:	Additional artwork for the Xfce
Summary(pl):	Dodatkowe ozdobniki dla Xfce
Name:		xfce4-artwork
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	b7612ee950fcf052e5acfacd0fda729f
URL:		http://xfce-goodies.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional artwork (backgrounds...) for the Xfce desktop environment.

%description -l pl
Dodatkowe ozdobniki (tapety...) dla ¶rodowiska Xfce.

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
