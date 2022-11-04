import zeep

# define a URL do WSDL (conversão de número para número por extenso)
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# Numero para conversao
number = 234456667

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=number
)
# imprime o resultado
print(result)
