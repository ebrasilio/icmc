


def cadastrar():
    # como armazenamento, precisa utilizar uma lista global
    # requisito: o sistema deve permitir o cadastro de no minimo 5 livros para validação inicial

    print("***Bem-vindo ao sistema de cadastramento ***\n")

    biblio = []

    titulo = input("Informe o título: ")
    autor = input("Informe o autor principal: ")
    ano = input("Informe o ano de publicação: ")
    assunto = input("Informe o assunto principal: ")
    status = "sim"
    aux = dict( zip( ["titulo", "autor", "ano", "assunto", "status"], 
                            [titulo, autor, ano, assunto, status] ))
    biblio.append(aux)
    return biblio

def consultar(titulo=None, autor=None, assunto=None):
    # busca por filtros implementar a busca por titulo ou autor
    pass

def saida():
    # mudar o status para indisponivel, "Não"
    pass

def entrada():
    # mudar status para "Sim" novamente
    pass



opt = int(input("Selecione a opção desejada: \n1- Cadastrar \n2- Consulta \n3- Empréstimo \n4- Devolução \n6- Saida\n"))
while opt != 6:
    if opt == 1:
        tt = cadastrar()
        print(tt)
    elif opt == 2:
        consultar()
    elif opt == 3:
        saida()
    elif opt == 4:
       entrada()
    opt = int(input("\nSelecione a opção desejada: \n1- Cadastrar \n2- Consulta \n3- Empréstimo \n4- Devolução \n6- Saida\n"))
print("Bye")
            




