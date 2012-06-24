Summary:	A weather plugin for gkrellm
Summary(pl):	Plugin pokazuj�cy pogod� dla gkrellm
Summary(pt_BR):	Um plugin gkrellm para acompanhamento das condi��es clim�ticas
Name:		gkrellm-weather
Version:	2.0.5
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/gkrellweather-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
URL:		http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/index.html
Requires:	perl
BuildRequires:	gkrellm-devel >= 2.0.0
BuildRequires:	gtk+2-devel
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

%description -l pl
GKrellWeather jest pluginem pokazuj�cym pogod� w GKrellM. Jego
w�asno�ci:

  - Wybieranie lokalizacji poprzez 4-literowy kod METAR.
  - Monitorowanie temperatury, dew point, ci�nienia, wilgotno�ci, stanu
    zachmurzenia, pr�dko�ci i kierunku wiatru.
  - Wy�wietlanie przy u�yciu systemu miar anglosaskich (stopnie
    Fareheighta, cale s�upa rt�ci, mile na godzin�) jak i metrycznego
    (stopnie Celsjusza, milimetry s�upa rt�ci, kilometry na godzin�)
  - wy�wietlanie ci�nienia w kPa, hPa i mmHg
  - wy�wietlanie pr�dko�ci wiatru w km/h, m/s i w skali Beauforta

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
CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/gkrellm2,%{_bindir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}/gkrellm2 \
	BINDIR=%{_bindir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(644,root,root) %{_libdir}/gkrellm2/gkrellweather.so
%attr(755,root,root) %{_bindir}/GrabWeather
