---
theme: default
size: 4:3
marp: true
paginate: true
_paginate: false
title: Aula 04: Autenticação
author: Diego Cirilo

---
<style>
img {
  display: block;
  margin: 0 auto;
}
</style>

# <!-- fit --> Programação Orientada a Serviços

### Prof. Diego Cirilo

**Aula 04**: Autenticação

---
# Autenticação
- Autenticação
    - Verifica identidade do usuário para o serviço.
- Autorização
    - Verifica as permissões de acesso do usuário.
- Necessária para controle de acesso às APIs
- Basic auth (HTTP)
- API Keys
- OAuth

---
# Basic Auth
- Usa o cabeçalho HTTP
- Necessário passar usuário e senha no request
- Mais simples
- Pouco segura

---
# Exemplo API Github
```python
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
  
response = requests.get('https://api.github.com/user',
            auth = HTTPBasicAuth('dvcirilo', password))
  
print(response.text)
print(response)
```

---
# API Keys
- Serviço disponibiliza as chaves
- Chave é passada no cabeçalho HTTP

---
# Exemplo SUAP

```python
import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]
print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

response = requests.get(api_url+"v2/minhas-informacoes/meus-dados/", json=data, headers=headers)

print(response.text)
print(response)
```

---
# OAuth

- Open Authorization
- Padrão aberto de serviços de autorização
- Usado na maioria dos serviços grandes, ex. Google, Facebook, Twitter, SUAP, etc.
- Aplicação deve ser registrada no serviço

---
# OAuth

![width:700px](../img/oauth.png)

---

# <!--fit--> Dúvidas? 🤔
