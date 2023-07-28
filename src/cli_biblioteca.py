from xml.dom.minidom import parse

dom = parse("biblioteca.xml")

# Elemento raiz do XML (biblioteca)
biblioteca = dom.documentElement

# Recebe uma lista dos elementos com tag "livro"
livros = biblioteca.getElementsByTagName('livro')

id_livro = 0
# Acessa as informações de cada livro
for livro in livros:
    id_livro+=1
    categoria = livro.getAttribute('categoria')
    elemento_titulo = livro.getElementsByTagName('título')[0]
    titulo = elemento_titulo.firstChild.nodeValue
    print(f'{id_livro} - {titulo}')

id_lido = int(input("Digite o id do livro para saber mais: "))
livro = livros[id_lido-1]
print("---\n")

elemento_titulo = livro.getElementsByTagName('título')[0]
titulo = elemento_titulo.firstChild.nodeValue
elemento_autor = livro.getElementsByTagName('autor')[0]
origem = elemento_autor.getAttribute('origem')
autor = elemento_autor.firstChild.nodeValue
elemento_ano = livro.getElementsByTagName('ano')[0]
ano = elemento_ano.firstChild.nodeValue

print("Categoria:", categoria)
print("Título:", titulo)
print(f'Autor: {autor} ({origem})')
print("Ano:", ano)
