Summary:	A weather plugin for gkrellm
Summary(pl):	Plugin pokazuj±cy pogodê dla gkrellm
Summary(pt_BR):	Um plugin gkrellm para acompanhamento das condições climáticas
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
GKrellWeather jest pluginem pokazuj±cym pogodê w GKrellM. Jego
w³asno¶ci:

  - Wybieranie lokalizacji poprzez 4-literowy kod METAR.
  - Monitorowanie temperatury, dew point, ci¶nienia, wilgotno¶ci, stanu
    zachmurzenia, prêdko¶ci i kierunku wiatru.
  - Wy¶wietlanie przy u¿yciu systemu miar anglosaskich (stopnie
    Fareheighta, cale s³upa rtêci, mile na godzinê) jak i metrycznego
    (stopnie Celsjusza, milimetry s³upa rtêci, kilometry na godzinê)
  - wy¶wietlanie ci¶nienia w kPa, hPa i mmHg
  - wy¶wietlanie prêdko¶ci wiatru w km/h, m/s i w skali Beauforta

%description -l pt_BR
Um plugin gkrellm para acompanhamento das condições climáticas,
inclui:

 - Escolha sua localização através de um código de identificação de 4
   letras (estação METAR)
 - Monitora temperatura, pressão, ponto de orvalho, umidade relativa,
   condições atmosféricas, direção e velocidade do vento
 - Mostrar usando o sistema imperial de medidas (graus Fareheight,
   polegadas de mercúrio, milhas por hora)
 - Mostrar usando o sistema métrico (graus Célsius, milímetros de
   mercúrio, kilômetros por hora)
 - Mostrar pressão em kPa, hPa e mmHg
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
