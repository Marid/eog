Summary:	The Eye of GNOME image viewer
Summary(pl.UTF-8):	Oko GNOME - przeglądarka obrazków
Summary(pt_BR.UTF-8):	Visualizador de imagem Eye of GNOME
Name:		eog
Version:	2.21.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	e83c34e7d9e3b94944dff3d3697cff1d
Patch0:		%{name}-codegen.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/eog/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	exempi-devel >= 1.99.2
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-desktop-devel >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-icon-theme >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	lcms-devel
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libexif-devel >= 1:0.6.14
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info >= 0.20
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.20.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eye of GNOME is a tool for viewing/cataloging images.

%description -l pl.UTF-8
Eye of GNOME (Oko GNOME) jest narzędziem do oglądania/katalogowania
obrazków.

%description -l pt_BR.UTF-8
Aplicativo para visualizar imagens chamado Eye of GNOME.

%package devel
Summary:	Header files for eog
Summary(pl.UTF-8):	Pliki nagłówkowe eog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.20.0
Requires:	gnome-vfs2-devel >= 2.20.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnomeui-devel >= 2.20.0

%description devel
Header files for eog.

%description devel -l pl.UTF-8
Pliki nagłówkowe eog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e "s#sr\@Latn#sr\@latin#" po/LINGUAS
mv po/sr\@{Latn,latin}.po

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

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install eog.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall eog.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/eog
%{_sysconfdir}/gconf/schemas/eog.schemas
%{_datadir}/%{name}
%{_desktopdir}/eog.desktop
%{_iconsdir}/hicolor/*/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/eog-2.20
%{_pkgconfigdir}/*.pc
