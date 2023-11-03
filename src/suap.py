import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
print(response.json())
token = response.json()["access"]

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

response = requests.get(api_url+"v2/minhas-informacoes/meus-dados/", json=data, headers=headers)

print(response.text)
print(response)
