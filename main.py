import json


def cadastrar():

    print("***Bem-vindo ao sistema de cadastramento ***\n")
    

    titulo = input("Informe o título: ")
    autor = input("Informe o autor principal: ")
    ano = input("Informe o ano de publicação: ")
    assunto = input("Informe o assunto principal: ")
    status = "sim"
    biblio = dict( zip( ["titulo", "autor", "ano", "assunto", "status"], 
                            [titulo, autor, ano, assunto, status] ))
    print (biblio)
    print(type(biblio))

    with open("biblioteca.json", "w+", encoding = "utf-8") as bib:
         json.dump(biblio, bib, ensure_ascii=False, indent=2)

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



opt = int(input("Selecione a opção desejada: \n1- Cadastrar \n2- Consulta \n3- Empréstimo \n4- Devolução \n6- Saida\n"))
while opt != 6:
    if opt == 1:
        cadastrar()
    elif opt == 2:
        consultar()
    elif opt == 3:
        saida()
    elif opt == 4:
       entrada()
    opt = int(input("\nSelecione a opção desejada: \n1- Cadastrar \n2- Consulta \n3- Empréstimo \n4- Devolução \n6- Saida\n"))
print("Bye")
            




