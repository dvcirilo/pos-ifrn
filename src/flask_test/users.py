import requests

# Definindo a classe users
class Users:
   
    # URL do serviço REST
    base_url = "https://jsonplaceholder.typicode.com/users/"

    def list(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido")

    def read(self, user_id):
        url = self.base_url+str(user_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido")

    def delete(self, user_id):
        url = self.base_url+str(user_id)
        response = requests.delete(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido")

    def create(self,user_data):
        url = self.base_url

        response = requests.post(url, json=user_data)

        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError("Problema na execução")

    def update(self, user_id, user_data):
        url = self.base_url+str(user_id)

        response = requests.patch(url, json=user_data)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Problema na execução")
