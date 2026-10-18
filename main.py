import json


def cadastrar():

    print("***Bem-vindo ao sistema de cadastramento ***\n")
    
    biblio = []
    titulo = input("Informe o título: ")
    autor = input("Informe o autor principal: ")
    ano = input("Informe o ano de publicação: ")
    assunto = input("Informe o assunto principal: ")
    status = "sim"
    biblio.append(
        dict( zip( ["titulo", "autor", "ano", "assunto","status"], [titulo, autor, ano, assunto, status] )))

    with open("biblioteca.json", "r+", encoding="utf-8") as file:
        dados = json.load(file)

    biblio.append(dados)

       
    with open("biblioteca.json", "w+", encoding = "utf-8") as file:
         json.dump(biblio, file, ensure_ascii=False, indent=2)


# def atualizar(biblio):
#     with open("biblioteca.json", "r+", encoding="utf-8") as arq:
#         biblioteca = json.load(arq)
    
#     with open("biblioteca.json", "w+", encoding = "utf-8") as bib:
#         json.dump(bib, biblio, ensure_ascii=False, ident=4)

#     return

def consultar(titulo=None, autor=None, assunto=None):
    # abrir o arquivo em formato json 
    # busca por filtros implementar a busca por titulo ou autor
    pass

def saida():
    # mudar o status para indisponivel, "Não"
    pass

def entrada():
    # mudar status para "Sim" novamente
    pass



opt = int(input("Selecione a opção desejada: \n1- Cadastrar \n2- Listar: \n3- Consulta \n4- Empréstimo \n5- Devolução \n6- Saida\n"))
while opt != 6:
    if opt == 1:
        cadastrar()
    elif opt == 2:
        listar()
    elif opt == 3:
        consultar()
    elif opt == 4:
        saida()
    elif opt == 5:
       entrada()
    opt = int(input("\nSelecione a opção desejada: \n1- Cadastrar \n2- Listar \n3- Consulta \n4- Empréstimo \n5- Devolução \n6- Saida\n"))
print("Bye")
            




