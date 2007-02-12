%include	/usr/lib/rpm/macros.perl
Summary:	A weather plugin for gkrellm
Summary(pl.UTF-8):   Plugin pokazujący pogodę dla gkrellm
Summary(pt_BR.UTF-8):   Um plugin gkrellm para acompanhamento das condições climáticas
Name:		gkrellm-weather
Version:	2.0.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/gkrellweather-%{version}.tgz
# Source0-md5:	73f5ec4e950f933a5904317037d6add2
Patch0:		%{name}-paths.patch
URL:		http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/index.html
BuildRequires:	gkrellm-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
GKrellWeather jest pluginem pokazującym pogodę w GKrellM. Jego
własności:

  - Wybieranie lokalizacji poprzez 4-literowy kod METAR.
  - Monitorowanie temperatury, punktu rosy, ciśnienia, wilgotności, stanu
    zachmurzenia, prędkości i kierunku wiatru.
  - Wyświetlanie przy użyciu systemu miar anglosaskich (stopnie
    Fareheighta, cale słupa rtęci, mile na godzinę) jak i metrycznego
    (stopnie Celsjusza, milimetry słupa rtęci, kilometry na godzinę)
  - wyświetlanie ciśnienia w kPa, hPa i mmHg
  - wyświetlanie prędkości wiatru w km/h, m/s i w skali Beauforta

%description -l pt_BR.UTF-8
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

%{__perl} -pi -e 's@lib/gkrellm2@%{_lib}/gkrellm2@' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fPIC `pkg-config --cflags gtk+-2.0`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/gkrellm2,%{_bindir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellweather.so
%attr(755,root,root) %{_bindir}/GrabWeather
