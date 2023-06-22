---
theme: default
size: 4:3
marp: true
paginate: true
_paginate: false
title: Aula 08: XML Schema
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

**Aula 08**: XML Schema

---
# XML Schema
- O DTD apresenta algumas limitações:
    - Não é escrito em XML, criando confusão com duas linguagens diferentes
    - Não suporta namespaces
    - Não suporta tipos de dados (string, integer, float, etc)
- O XML Schema Definition (XSD) é uma recomendação do W3C que soluciona essas limitações.
- De forma geral é um XML que descreve os componentes de outro XML (ou uma classe deles).

---
# XML Schema
- Tipos de dados são importantes para garantir integridade dos dados. Ex.
    - Como garantir que `<data></data>` tenha uma data com DTD? E como garantir um padrão na escrita dessa data?
- Também há problemas com o XSD:
    - A ordem continua importando (nem sempre é necessário)
    - Muito complexa (a primeira parte da especificação tem 150 páginas)
    - ...

---
# Exemplo
- XML
```xml
 <cartao xmlns="http://cartaodevisitas.org" 
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://cartaodevisitas.org 
                           cartao.xsd">
   <nome>Luiz Silva</nome>
   <titulo>Gerente, Lojas Pernambucanas S.A.</titulo>
   <email>luiz.silva@pernambucanas.com.br</email>
   <telefone>(88)99456-1414</telefone>
   <logo url="logo.gif"/>
 </cartao>
```

---
# Exemplo
- XSD (cartao.xsd)
```xml
<schema xmlns="http://www.w3.org/2001/XMLSchema"
        xmlns:b="http://cartaodevisitas.org"
        targetNamespace="http://cartaodevisitas.org">

  <element name="cartao" type="b:cartao_type"/>
  <element name="nome" type="string"/>
  <element name="titulo" type="string"/>
  <element name="email" type="string"/>
  <element name="telefone" type="string"/>
  <element name="logo" type="b:logo_type"/>

  <complexType name="cartao_type">
    <sequence>
      <element ref="b:nome"/>
      <element ref="b:titulo"/>
      <element ref="b:email"/>
      <element ref="b:telefone" minOccurs="0"/>
      <element ref="b:logo" minOccurs="0"/>
    </sequence>
  </complexType>

  <complexType name="logo_type">
    <attribute name="url" type="anyURI"/>
  </complexType>

</schema>
```

---
# Sintaxe
- O elemento raiz do XSD é o `<schema>`
- Alguns possíveis atributos do `<schema>`:
    - `xmlns="http://www.w3.org/2001/XMLSchema"` namespace do XML Schema padrão.
    - `xmlns:b="http://cartaodevisitas.org"` define o prefixo `b` para o namespace do cartão.
    - `targetNamespace="http://cartaodevisitas.org"` indica qual namespace que esse XSD descreve.

---
# Sintaxe
- Para incluir o XSD no XML:
    - `xmlns="http://cartaodevisitas.org"` namespace padrão.
    - `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"` namespace da instância do XSD.
    - `xsi:schemaLocation="http://cartaodevisitas.org cartao.xsd"` chamada do arquivo XSD.
        - O primeiro argumento é o namespace, e o segundo o arquivo
        - Perceba o uso do prefixo `xsi`

---
# Sintaxe
- Elementos *simples*
- Armazena apenas um dado (não tem sub-elementos)
    - `<element name="nome" type="tipodedado"/>`
- Exemplos de tipos de dados padrão:
    - `string`, `decimal`, `integer`, `boolean`, `date`, `time`, ...
- É possível definir tipos customizados.

---
# Restrições
- É possível limitar valores usando restrições ou *facets*.
- Ex.
```xml
<element name="idade">
  <simpleType>
    <restriction base="integer">
      <minInclusive value="0"/>
      <maxInclusive value="120"/>
    </restriction>
  </simpleType>
</element>
```

---
# Restrições
- Algumas possibilidades:
    - `length`, `minLength`, `maxLength`
    - `maxInclusive`, `maxExclusive`, `minInclusive`, `minExclusive`
    - `totalDigits`, `fractionDigits`
    - `pattern`
    - `enumeration`
    - `whiteSpace`

---
# Restrições
```xml
<element name="percentual">
    <simpleType>
        <restriction base="string">
            <pattern value="([0-9]|[1-9][0-9]|100)%"/>
        </restriction>
    </simpleType>
</element>
```

```xml
<element name="marca">
  <simpleType>
    <restriction base="string">
      <enumeration value="Audi"/>
      <enumeration value="Fiat"/>
      <enumeration value="BMW"/>
    </restriction>
  </simpleType>
</element>
```
---
# Tipos simples customizados
- Para possibilitar o reuso das restrições, é possível criar tipos customizados.
```xml
<element name="aproveitamento" type="percentual"/>

<simpleType name="percentual">
    <restriction base="string">
        <pattern value="([0-9]|[1-9][0-9]|100)%"/>
    </restriction>
</simpleType>
```

---
# Exemplos
```xml
<element name="idade" type="limite_idade">
<simpleType name="limite_idade">
    <restriction base="integer">
        <minInclusive value="0"/>
        <maxInclusive value="120"/>
    </restriction>
</simpleType>
```
```xml
<simpleType name="tamanho">
    <restriction base="string">
        <pattern value="PP|P|M|G|GG"/>
    </restriction>
</simpleType>
```

---
# Elementos *complexos*
- Permitem a definição de elementos com sub-elementos e atributos
- Podem ser vazios ou conter elementos, texto ou elementos e texto
```xml
<produto id="p123"/>

<funcionário>
    <nome>James Bond</nome>
    <matrícula>007</matrícula>
</funcionário>

<comida tipo="sobremesa">Sorvete</comida>
```
---
# Elementos *complexos*
```xml
<element name="funcionário">
  <complexType>
    <sequence>
      <element name="matrícula" type="integer"/>
      <element name="nome" type="string"/>
    </sequence>
  </complexType>
</element>
```

---
# Elementos *complexos* - reuso
```xml
<element name="funcionário" type="cadPessoa"/>
<element name="aluno" type="cadPessoa"/>

<complexType name="cadPessoa">
    <sequence>
        <element name="matrícula" type="integer"/>
        <element name="nome" type="string"/>
    </sequence>
</complexType>
```

---
# Elementos *complexos* - extensão
```xml
<complexType name="cadPessoa">
    <sequence>
        <element name="matrícula" type="integer"/>
        <element name="nome" type="string"/>
    </sequence>
</complexType>

<complexType name="cadPessoaCompleto">
  <complexContent>
    <extension base="cadPessoa">
      <sequence>
        <element name="endereço" type="string"/>
        <element name="cidade" type="string"/>
        <element name="país" type="string"/>
      </sequence>
    </extension>
  </complexContent>
</complexType>
```

---
# Cardinalidade
- `maxOccurs` e `minOccurs`
- `maxOccurs="unbounded"` para infinitas ocorrências
```xml
<complexType name="cadPessoa">
    <sequence>
        <element name="matrícula" type="integer"/>
        <element name="nome" type="string"/>
        <element name="telefone" type="string" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
</complexType>

```

---
# Exercício
- Crie um XML Schema básico para um prato (elemento raiz) que tenha os elementos: 
    - `nome` (string com 100 caracteres no máximo)
    - `refeição` (`café`, `almoço` ou `janta`)
    - `ingredientes` com os sub-elementos `ingrediente` (pelo menos um)
    - `preço` (decimal com duas casas)
    - `dataCadastro` (data)
- Crie um XML que use o schema acima e valide no VS Code.

---
# Atributos
- Elementos *simples* não tem atributos.
- Atributos são opcionais por padrão, é preciso utilizar `use="required"` para ser obrigatório.
- `<attribute name="nome" type="tipodedado" use="required"/>`

---
# Exemplos
- [Nota Fiscal Eletrônica](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=BMPFMBoln3w=)

---
# <!--fit--> Dúvidas? 🤔
