Summary:	a weather plugin for gkrellm
Summary(es):	a weather plugin for gkrellm
Summary(pl):	plugin pokazuj�cy pogod� dla gkrellm
Summary(pt_BR):	Um plugin gkrellm para acompanhamento das condi��es clim�ticas
Name:		gkrellm-weather
Version:	0.2.3a
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.cs.usyd.edu.au/~franky/repository/c/gkrellm/gkrellweather-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Requires:	perl
BuildRequires:	gkrellm-devel >= 1.0.2
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GKrellWeather is a weather plugin for GKrellM. Its features include:

  - Choose your own location by 4-letter METAR station identifier code.
  - Monitor temperature, dew point, pressure, relative humidity, sky
    condition, wind direction and speed
  - Display using imperial units (degrees Fareheight, inches of Mercury,
    miles per hour)
  - Display using metric units (degrees Celsius, millimeters of Mercury,
    kilometers per hour)
  - Display pressure in kPa, hPa and mmHg
  - Display wind speeds in kmph, mps and beaufort scale

%description -l es
GKrellWeather is a weather plugin for GKrellM. Its features include:

  - Choose your own location by 4-letter METAR station identifier code.
  - Monitor temperature, dew point, pressure, relative humidity, sky
    condition, wind direction and speed
  - Display using imperial units (degrees Fareheight, inches of Mercury,
    miles per hour)
  - Display using metric units (degrees Celsius, millimeters of Mercury,
    kilometers per hour)
  - Display pressure in kPa, hPa and mmHg
  - Display wind speeds in kmph, mps and beaufort scale

%description -l pl
GKrellWeather jest plugin'em pokazuj�cym pogod� w GKrellM. Jego
w�asno�ci:

  - Wybieranie lokalizacji poprzez 4-literowy kod METAR.
  - Monitorowanie temperatury, dew point, ci�nienia, wilgotno�ci, stanu
    zachmurzenia, pr�dko�ci i kierunku wiatru.
  - Wy�wietlanie przy u�yciu systemu miar anglosaskich (stopnie
    Fareheight'a, cale s�upa rt�ci, mile na godzin�) jak i metrycznego
    (stopnie Celsiusza, milimetry s�upa rt�ci, kilometry na godzin�)
  - wy�wietlanie ci�nienia w kPa, hPa i mmHg
  - wy�wietlanie pr�dko�ci wiatru w km/h, m/s i w skali Beaufort'a

%description -l pt_BR
Um plugin gkrellm para acompanhamento das condi��es clim�ticas,
inclui:

 - Escolha sua localiza��o atrav�s de um c�digo de identifica��o de 4
   letras (esta��o METAR)
 - Monitora temperatura, press�o, ponto de orvalho, umidade relativa,
   condi��es atmosf�ricas, dire��o e velocidade do vento
 - Mostrar usando o sistema imperial de medidas (graus Fareheight,
   polegadas de merc�rio, milhas por hora)
 - Mostrar usando o sistema m�trico (graus C�lsius, mil�metros de
   merc�rio, kil�metros por hora)
 - Mostrar press�o em kPa, hPa e mmHg
 - Mostrar velocidade do vendo em kmph, mps e escala beaufort

%prep
%setup -q -n gkrellweather-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/gkrellm,%{_bindir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}/gkrellm \
	BINDIR=%{_bindir} install

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(644,root,root) %{_libdir}/gkrellm/gkrellweather.so
%attr(755,root,root) %{_bindir}/GrabWeather
