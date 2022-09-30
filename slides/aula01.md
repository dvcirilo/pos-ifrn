---
theme: gaia
size: 4:3
---
# Programação Orientada a Serviços 2022.2
## Prof. Diego Cirilo
---
# Ementa (segunda parte)
 - 5. Programação de serviços
   - 5.1. Implementação de serviços
   - 5.2. Instalação e manutenção de webservices
   - 5.3. Integração de aplicações em diferentes tecnologias
 - 6. Programação de clientes
   - 6.1. Programação de Clientes Desktop
   - 6.2. Programação de Clientes Móveis
---
# Conhecimentos
  - Protocolo HTTP
  - HTML
  - JavaScript - DOM (Document-Object Model)
  - Python/Django
---
# APIs e WebServices
  - Application Programming Interfaces
  - Web Services: caso especial
---
# Protocolo HTTP
  - Hyper text transfer protocol
  - Camada de aplicação
  - Baseado no modelo cliente-servidor
  - Padrão de mensagens de requisição e respostas
  - Porta 80 (ou 443 para HTTPS)
---
# Métodos HTTP
| Método | Descrição |
|-------|------|
| GET | Recebe um recurso existente |
| POST | Cria um novo recurso |
| PUT | Atualiza um recurso existente |
| PATCH | Atualiza parcialmente um recurso existente |
| DELETE | Remove um recurso |
---
# Códigos de status
| Faixa | Categoria 
|-------|------|
| 2xx | Sucesso |
| 3xx | Redirecionamento |
| 4xx | Erro de cliente |
| 5xx | Erro de servidor |
---
# Códigos de status
| Código | Significado                | Descrição                                                                    |
|------|------------------------|--------------------------------------------------------------------------------|
| 200  | OK                     | The requested action was successful.                                           |
| 201  | Created                | A new resource was created.                                                    |
| 202  | Accepted               | The request was received, but no modification has been made yet.               |
| 204  | No Content             | The request was successful, but the response has no content.                   |
| 400  | Bad Request            | The request was malformed.                                                     |
| 401  | Unauthorized           | The client is not authorized to perform the requested action.                  |
| 404  | Not Found              | The requested resource was not found.                                          |
| 415  | Unsupported Media Type | The request data format is not supported by the server.                        |
| 422  | Unprocessable Entity   | The request data was properly formatted but contained invalid or missing data. |
| 500  | Internal Server Error  | The server threw an error when processing the request.                         |

# REST e SOAP
  - Representational State Transfer
  - Métodos HTTP
  - Payload (Carga útil)
  - Simple Object Access Protocol
---
# AJAX
  - Asynchronous Javascript and XML

