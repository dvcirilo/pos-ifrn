import requests
import xmltodict

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado (solicita nome da moeda do BR)
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<CountryCurrency xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>BR</sCountryISOCode>
					</CountryCurrency>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST, com o XML como data
response = requests.request("POST", url, headers=headers, data=payload)

# Converte o XML recebido (response.text) em um dict
dictdata = xmltodict.parse(response.text)

# Seleciona o dado desejado dentro do dict e imprime
print(dictdata["soap:Envelope"]["soap:Body"]["m:CountryCurrencyResponse"]["m:CountryCurrencyResult"]["m:sName"])
