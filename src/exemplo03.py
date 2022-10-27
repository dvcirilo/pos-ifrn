#!/usr/bin/env python3

import requests
import xmltodict
import json
from xml.dom.minidom import parse, parseString

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

# imprime a resposta
outdict = xmltodict.parse(response.text)
print(outdict["soap:Envelope"]["soap:Body"])

data = parseString(response.text)
print(data.getElementsByTagName("m:sISOCode")[0].childNodes)

print(response)
