


def cadastrar(titulo, autor, ano, status):
    # criar um dicionário com os dados, status de disponibilidade = "Sim"
    # como armazenamento, precisa utilizar uma lista global
    # requisito: o sistema deve permitir o cadastro de no minimo 5 livros para validação inicial
    pass

def listar():
    # percorrer a lista de livros e exibir os detalhes de cada um de forma organizada
    pass

def consultar(titulo=None, autor=None):
    # busca por filtros implementar a busca por titulo ou autor
    pass

def saida():
    # mudar o status para indisponivel, "Não"
    pass

def entrada():
    # mudar status para "Sim" novamente
    pass



opt = int(input("Selecione a opção desejada: \n1- Cadastrar \n2- listar \n3- Consulta \n4- Empréstimo \n5- Devolução \n6- Saida\n"))

while opt != 6:
    if opt == 1:
        cadastrar(titulo, autor, edição, status)
    if opt == 2:
        listar()
    if opt == 3:
        consultar(titulo, autor)
    if opt == 4:
        saida()
    if opt == 5:
       entrada()
print("Bye")
            




