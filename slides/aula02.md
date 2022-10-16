---
theme: default
size: 4:3
paginate: true
_paginate: false
title: Aula 02: APIs REST
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

**Aula 02**: APIs REST

---
# REST e SOAP
  - Representational State Transfer
  - Métodos HTTP
  - Payload (Carga útil)
  - Simple Object Access Protocol

---
# Princípios do REST
- Interface Uniforme
    - Identificação de recursos
    - Manipulação de recursos através de representações
    - Mensagens auto-descritivas
    - Uso de hyperlinks 
- Cliente - Servidor
- *Stateless*
- *Cacheable*
- Sistema em camadas

<!--
Identification of resources – The interface must uniquely identify each resource involved in the interaction between the client and the server.

Manipulation of resources through representations – The resources should have uniform representations in the server response. API consumers should use these representations to modify the resources state in the server.

Self-descriptive messages – Each resource representation should carry enough information to describe how to process the message. It should also provide information of the additional actions that the client can perform on the resource.

Hypermedia as the engine of application state – The client should have only the initial URI of the application. The client application should dynamically drive all other resources and interactions with the use of hyperlinks.
-->
---
# Interagindo com API REST

- Uma API REST expõe URLs públicas que as aplicações podem acessar
- *API Endpoints*

---

# RESTful resources
<style scoped>
table {
  font-size: 20px;
}
</style>

|Método HTTP | API endpoint | Descrição |
|---|---|---|
|GET	|/clientes	                |Lista clientes.|
|GET	|/clientes/<cliente_id>	|Cliente específico.|
|POST	|/clientes	                |Cria um novo cliente.|
|PUT	|/clientes/<cliente_id>	|Atualiza um cliente.|
|PATCH	|/clientes/<cliente_id>	|Atualiza parcialmente um cliente.|
|DELETE	|/clientes/<cliente_id>	|Remove um cliente.|

---

# Exemplos
- https://suap.ifrn.edu.br/api/docs/ 
- https://developer.twitter.com/en/docs/api-reference-index
- https://docs.github.com/en/rest

---
# Interagindo com APIs REST em Python

 - Biblioteca `requests`

 ```shell
 $ pip install requests
 ```
---
# GET

```python
import requests
api_url = "https://api.github.com/users/dvcirilo"
response = requests.get(api_url)
print(response.json())
```
---
# Métodos do objeto `Response`
```python
response.status_code
response.headers
response.json()
```
---
# POST

- API pública que aceita posts: https://jsonplaceholder.typicode.com/todos

```json
{
    "userId": 1,
    "title": "Comprar farinha",
    "completed": false
}
```
---
# POST
```python
import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Comprar farinha", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)

```

---

# PUT
```python
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Lavar carro", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

```

---

# PATCH

```python
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Cortar grama"}
response = requests.patch(api_url, json=todo)
print(response.json())
```

---
# DELETE

```python
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
```

---
# Prática

- Acesse a documentação do jsonplaceholder.typicode.com
- Explore as operações com os recursos aninhados, exemplo:
    - *to-dos* do usuário 3
    - comentários do post 3
- Identifique os atributos através do navegador

---
# Prática

- Implemente uma CLI para CRUD das *to-dos*
- Apresente as opções de:
    - Listar usuários
    - Listar as tarefas do usuário
    - Criar/Ler/Atualizar/Deletar usuários
    - Criar/Ler/Atualizar/Deletar tarefas de usuário

---
# API *Wrappers*
- Bibliotecas de mais alto nível para acesso a APIs
- Continuam usando URLs, json, requests, etc...
- Simplificam a operação para o dev
- Ex. `python-twitter`, `pygithub`

---
# Prática
- Desenvolva um wrapper para a API dos *users*
- Exemplo de uso:
```python
import users-wrapper as users

user = users.read(user_id)
print(user["name"])

users-list = users.list()

users.delete(user_id)
```

---
# <!--fit--> Dúvidas? 🤔
