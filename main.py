import os
import json


def cadastrar():
    # Função cadastrar, recebe os atributos do livro, se o arquivo bibloteca.json
    # existe, inclui o novo volume e salva. Se ainda não existe, a função cria.

    print("Cadastramento\n")
    titulo = input("Informe o título: ")
    autor = input("Informe o autor principal: ")
    ano = input("Informe o ano de publicação: ")
    assunto = input("Informe o assunto principal: ")
    status = "sim"

    aux = dict( 
        {"titulo": titulo, "autor": autor, "ano": ano, "assunto": assunto, "status": status})
    
    if os.path.exists("biblioteca.json"):
        with open("biblioteca.json", "r", encoding="utf-8") as file:
            biblioteca = json.load(file)
        biblioteca.append(aux)

        with open("biblioteca.json", "w", encoding = "utf-8") as file:
            json.dump(biblioteca, file, ensure_ascii=False, indent=2)
    else:
        biblioteca = [aux]
        with open("biblioteca.json", "w", encoding = "utf-8") as file:
            json.dump(biblioteca, file, ensure_ascii=False, indent=2)
        


def listar():
    # ler o arquivo biblioteca.json e formatar uma tabela na tela
    with open("biblioteca.json", "r+", encoding="utf-8") as file:
            dados = json.load(file)
    
    for i in range(0,len(dados)):
        print(dados[i]["titulo"] + "\t" + dados[i]["autor"])

  


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


print("\n*** Bem vindo ao SisBiBra - Sistema de Bibliotecas Brasilio ***\n")
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
            




