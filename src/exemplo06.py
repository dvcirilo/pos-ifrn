import requests
import untangle

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado
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
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# Converte o XML para um objeto untangle
unt_obj = untangle.parse(response.text)

# Filtra a tag com o dado desejado e imprime o conteúdo
print(unt_obj.soap_Envelope.soap_Body.m_CountryCurrencyResponse.m_CountryCurrencyResult.m_sName.cdata)
