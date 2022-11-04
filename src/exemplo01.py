#!/usr/bin/env python3

import requests

base_url = "https://jsonplaceholder.typicode.com/"

def list_users():
    url = base_url+"users/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("ID inválido")

def read_user(user_id):
    url = base_url+"users/"+str(user_id)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("ID inválido")

def list_user_todos(user_id):
    url = base_url+"users/"+str(user_id)+"/todos"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("ID inválido")

def create_user(user_data):
    url = base_url+"users/"

    response = requests.post(url, json=user_data)
    print(response.status_code)

    if response.status_code == 201:
        return response.json()
    else:
        raise ValueError("Problema na execução")

print("Digite 1 para listar usuários")
print("Digite 2 para listar tarefas dos usuários")
print("Digite 3 para criar usuários")
print("Digite 4 para ler dados de um usuário")
opcao = int(input())
if opcao == 1:
    print(list_users())
elif opcao == 2:
    user_id = input("Digite o id do usuário: ")
    print(list_user_todos(int(user_id)))
elif opcao == 3:
    user_name = input("Digite o nome o usuario: ")
    user_email = input("Digite o email do usuario: ")
    user_data = {"name":user_name, "email":user_email}
    print(create_user(user_data))
elif opcao == 4:
    user_id = input("Digite o id do usuário: ")
    print(read_user(int(user_id)))
else:
    print("Opção inválida")

























