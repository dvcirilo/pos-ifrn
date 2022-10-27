import zeep

# define a URL do WSDL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# define a URL do método
method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"

# define a URL do serviço
service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# cria o header
header = zeep.xsd.Element(
	"Header",
	zeep.xsd.ComplexType(
		[
			zeep.xsd.Element(
				"{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
			),
			zeep.xsd.Element(
				"{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
			),
		]
	),
)
# define o valor do header a partir do objeto header
header_value = header(Action=method_url, To=service_url)

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
country_code = "BR"

# faz a chamada do serviço
result = client.service.CountryIntPhoneCode(
	sCountryISOCode=country_code,
	_soapheaders=[header_value]
)
# imprime o resultado
print(f"O código de telefone do {country_code} é {result}")

# define o código do país para US
country_code = "US"

# faz a chamada do serviço
result = client.service.CountryIntPhoneCode(
	sCountryISOCode=country_code,
	_soapheaders=[header_value]
)

# imprime o resultado
print(f"O código de telefone do {country_code} é {result}")
