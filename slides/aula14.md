---
theme: default
size: 4:3
marp: true
paginate: true
_paginate: false
title: Aula 14: Clientes JavaScript
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

**Aula 14**: Clientes JavaScript

---
# Introdução
- Usualmente as funcionalidades de um sistema web estão no servidor
- O servidor recebe as requisições, processa/acessa dados e *monta* o HTML
- As páginas HTML são enviadas *prontas* para o cliente (navegador)
- Depois de enviado ao cliente, o servidor não tem mais controle sobre a página
- *Front-end* - interface gráfica do usuário
- Como *desacoplar* a interface de usuário do servidor?

---
# JavaScript

- Linguagem *interpretada*, com tipagem dinâmica e multi-paradigma
- Desenvolvida nos anos 90 para dinamizar páginas web
- Permite alterar o conteúdo da página no lado do cliente
- É executada por uma *engine* no navegador
- Em meados dos anos 2000 surgiram os *runtimes* nativos, como o Node.js

---
# Versões do JavaScript

- Padrão ECMAScript (*European Computer Manufacturers Association*)
- Iniciais
    - ECMAScript 1 (1997): Primeira versão padronizada para compatibilidade entre navegadores.
    - ECMAScript 3 (1999): Introduziu tratamento de erros, expressões regulares e estabeleceu a base do JavaScript moderno.

---
# Versões do JavaScript

- ECMAScript 5 (2009)
    - Adicionou modo estrito, suporte a JSON e métodos de arrays (map, filter, reduce).

- ECMAScript 6 (ES6, 2015)
  - Let/Const (variáveis de escopo de bloco).
  - Funções de seta (arrow functions).
  - Classes e módulos.
  - *Promises* para operações assíncronas.

---
# Recursos Modernos do JavaScript

- ECMAScript 2016-2017 (ES7 & ES8)
    - ES7 (2016): Adicionou `Array.prototype.includes()` e o operador de exponenciação (`**`).
    - ES8 (2017): Introduziu async/await e métodos de objeto como `Object.entries()`.

- ECMAScript 2018-2023 (ES9 a ES13)
    - Operadores spread/rest para objetos.
    - Encadeamento opcional (`?.`) e operador de coalescência nula (`??`).
    - Top-level await para simplificar operações assíncronas.


---
# Runtimes do JS

- Node.js
    - Ambiente de execução de JavaScript *server-side*.
    - Utiliza a *engine* V8 do Chrome.
    - Oferece APIs para acessar o sistema de arquivos, redes e outras funcionalidades do servidor.

- Browser Engines
    - V8 (Chrome, Edge), SpiderMonkey (Firefox), JavaScriptCore (Safari).
    - Executam JavaScript diretamente nos navegadores, oferecendo suporte para aplicações web interativas.

---
# *Bundling*
- Webpack

---
# Tipo de dados

---
# Strings

---
# Manipulação da DOM
- *Document Object Model*
- Uma das principais funções do JS é manipular a DOM
- Criar/remover elementos, substituir conteúdo, alterar atributos, etc

---
# jQuery

---
# Eventos JS
- Os eventos reagem a ações do usuário, servidor ou temporizadas
- Permitem a execução de funções quando algo acontece
- Ex. `click`, `hover`, etc.

---
# Funções no JS
- A sintaxe para declarar funções mudou 

---
# Declarativo x Imperativo


---
# Referências
- https://javascript.info/
- https://developer.mozilla.org/pt-BR/docs/Web/JavaScript
- https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript

---
# <!--fit--> Dúvidas? 🤔
