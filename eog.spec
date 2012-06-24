Summary:	The Eye of GNOME image viewer
Summary(pl):	Oko GNOME - przegl�darka obrazk�w
Summary(pt_BR):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.16.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/eog/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	bba4f238aaac797b5a8e150aa55c7fb3
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-desktop-devel >= 2.16.1
BuildRequires:	gnome-vfs2-devel >= 2.16.1
BuildRequires:	intltool >= 0.35
BuildRequires:	lcms-devel
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	libgnomeui >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch1 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__gnome_doc_common}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{tk,ug}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install eog.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall eog.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/eog.schemas
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
