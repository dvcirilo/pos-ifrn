---
theme: default
size: 4:3
marp: true
paginate: true
_paginate: false
title: Aula 04 - Extra: Flask
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

**Aula 04 - Extra**: Flask

---
# Flask
- Framework leve para sistemas web em Python
- Mais simples que o Django para aplicações pequenas
- Mais responsabilidade nas mãos do dev

---
# Exemplo Básico
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello, world! </h1>"
```

Salve como `app.py`, `flask run` e acesse em http://localhost:5000

---
# Templates
- O Flask usa a engine de templates [Jinja2](https://palletsprojects.com/p/jinja/)
- Os templates por padrão ficam na pasta `templates`
- Ex. `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>FlaskApp</title>
</head>
<body>
    <h1>Aplicação Flask</h1>
    <h2>Meu belo site no Flask.</h2>
    <h3>{{ variavel }}</h3>
</body>
</html>
```
---
# Templates
- Para carregar o template em `app.py`
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    texto = "Variável passada como parâmetro para o template!!"
    return render_template('index.html', variavel=texto)
```
---
# Herança de templates
- Faz sentido criar um template base e atualizar apenas o conteúdo
- Ex. `templates/base.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %} {% endblock %}</title>
  </head>
  <body>
    <h1><a href="{{ url_for('index')}}">Meu Belo Site</a></h1>

    <div class="container">
        {% block content %} {% endblock %}
    </div>

  </body>
</html>
```
---
# Página de conteúdo
```html
{% extends 'base.html' %}

{% block content %}
{% block title %} Título do Meu Belo Site {% endblock %}
    <h2> Conteúdo do meu belo site! </h2>
{% endblock %}
```
---
# Laços
- No template
```html
{% for comment in comments %}
    <p>{{ comment }}</p>
{% endfor %}
```

- No `app.py`
```python
comments = ['comment a', 'comment b', 'comment c']
render_template('comments.html',comments=comments)
```
---
# Condicionais
- No template
```html
{% for user in users %}
    {% if user['funcao'] == 'admin' %}
        {% set bg_color = 'red' %}
    {% else %}
        {% set bg_color = 'white' %}
    {% endif %}
    <p style="background-color: {{ bg_color }}">{{ comment }}</p>
{% endfor %}
```

- No `app.py`
```python
users = [
{'nome':'Jonas', 'funcao':'admin'}, 
{'nome':'James', 'funcao':'user'}, 
{'nome':'Jairo', 'funcao':'user'}, 
]
render_template('users.html',users=users)
```
---
# Forms
- No template
```html
<form action="{{ url_for('create') }}" method="post">
    Nome: <input type="text" name="user_name"><br>
    Email: <input type="email" name="user_email"><br>
    <input type="submit" value="Enviar">
</form>
```
- No `app.py`
```python
@app.route('/user/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if not request.form['user_name']:
            flash('O nome é obrigatório!')
        else:
            user_data=user_api.create(request.form)
            return render_template('user.html', user_data=user_data)
    return render_template('create.html')
```
---
# Tarefa

Com base na classe criada na tarefa da Aula 02 (api wrapper) desenvolva um cliente para a API de To-Dos e Usuários.




