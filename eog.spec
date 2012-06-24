Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl�darka obrazk�w
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	0.118.0
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/eog/%{name}-%{version}.tar.bz2
Source1:	%{name}.gif
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	gnome-vfs2-devel >= 1.9.12
BuildRequires:	libgnomeprint-devel >= 1.112.0
BuildRequires:	libgnomeui >= 1.115.0
BuildRequires:	libbonoboui >= 1.115.0
BuildRequires:	bonobo-activation-devel >= 0.9.7
BuildRequires:	librsvg-devel >= 1.1.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _sysconfdir     /etc/X11/GNOME2
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl
Eye of GNOME (Oko GNOME) jest narz�dziem do ogl�dania/katalogowania
obrazk�w.

%description -l pt_BR
Aplicativo para visualizar imagens chamado Eye of GNOME.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
sed -e 's/-ourdir/ourdir/' xmldocs.make >xmldocs.make.tmp
mv xmldocs.make.tmp xmldocs.make
gettextize --copy --force
libtoolize --copy --force
intltoolize --copy --force
aclocal -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--enable-platform-gnome-2
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome

%post
/usr/bin/scrollkeeper-update
GCONF_CONFIG_SOURCE="" gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun
/usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
