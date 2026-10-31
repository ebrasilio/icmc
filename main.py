import os
import json

def open_bibliteca():
    with open("biblioteca.json", "r+", encoding="utf-8") as file:
        biblioteca = json.load(file)
    return biblioteca


def save_biblioteca(biblioteca):
    with open("biblioteca.json", "w", encoding = "utf-8") as file:
        json.dump(biblioteca, file, ensure_ascii=False, indent=2)

    
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
        biblioteca = open_bibliteca()
        biblioteca.append(aux)
        save_biblioteca(biblioteca)
        
    else:
        biblioteca = [aux]
        save_biblioteca(biblioteca)

        
def listar():
    # função listar, mostra todos os livros cadastrados na tela

    biblioteca = open_bibliteca()
    print ("_"*96)
    print(f"{"ACERVO:":^96}")
    for i in range(len(biblioteca)):
        print("id=" , i, "Titulo=", f"{biblioteca[i]["titulo"]:<38}", "Autor=", f"{biblioteca[i]["autor"]:<20}", "Disponível?", f"{biblioteca[i]["status"]}")
    print("\n")


def consultar(arg):
    # busca por filtros implementar a busca por titulo , autor ou assunto
    
    biblioteca = open_bibliteca()
    
    print ("_"*96)
    achado = False
    for i in range(len(biblioteca)):
        if arg in biblioteca [i]["titulo"] or arg in biblioteca [i]["autor"] or arg in biblioteca [i]["assunto"]:
             print("id=" , i, "Titulo=", f"{biblioteca[i]["titulo"]:<38}", "Autor=", f"{biblioteca[i]["autor"]:<20}", "Disponível?", f"{biblioteca[i]["status"]}")
             achado = True
    if achado == False:
        print("--> Termo "+arg+" não encontrado")


def saida(id):
    # função que altera o status do exemplar, caso ele seja emprestado

    biblioteca = open_bibliteca()
    try:
        levar = input("--> Confirma retirada do título? (S/N):")
        if levar == "S":
            if biblioteca[id]["status"] == "não":
                print("--> Livro já emprestado, saída não autorizada\n")
            else:
                biblioteca[id]["status"] = "não"
                print("--> Livro retirado com sucesso\n")
                save_biblioteca(biblioteca)
        else:
            print("--> Saída não realizada")
    except IndexError:
        print("--> Id incorreto. Verifique antes de prosseguir!!\n")


def entrada(id):
    # função que altera o status do exemplar quando ele é devolvido

    biblioteca = open_bibliteca()
    try:
        if biblioteca[id]["status"] == "não":
            biblioteca[id]["status"] ="sim"
            print("--> Livro de volta ao acervo")
            save_biblioteca(biblioteca)
        else:
            print("--> Livro encontra-se no nosso acervo, Verifique Id:")
    except IndexError:
            print("--> Id incorreto. Verifique antes de prosseguir!!\n")
      

def relatorio():
    # mostrar o total de livros cadastrados, quantos estão disponiveis e quantos estão emprestados 

    biblioteca = open_bibliteca()
    c_sim=0
    c_nao=0

    for i in range(len(biblioteca)):
        if biblioteca[i]["status"] == "sim":
            c_sim += 1
        else:
            c_nao += 1

    print("-"*25)
    print(f"{'Relatório':^25}", f"{"\nEmprestados: ":<20}" + f"{c_nao:>5}", f"{"\nDisponíveis: ":<20}" + f"{c_sim:>5}", f"{"\nTotal do Acervo:":<20}" + f"{(c_sim + c_nao):>5}")

def delete(id):
    # função que aposenta livros do acervo
    book = open_bibliteca()
    try:
        print("Tem certeza que quer excluir este livro? (S/N)\n",  book[id])
        remove = input() 
        if remove == "S":
            book.pop(id)
            save_biblioteca(book)
        else:
            print( "--> Exemplar náo removido\n")
    except IndexError:
        print("--> Id incorreto. Verifique antes de prosseguir!!\n")
    
#----- Programa Principal -----#
print("\n*** Bem vindo ao SisBiBra - Sistema de Bibliotecas Brasilio ***\n")
opt = int(input("Selecione a opção desejada: \n1- Cadastrar          (para incluir livros novos) \n2- Listar             (lista todo o acervo) \n3- Consulta           (consulta em título, autor ou assunto) \n4- Empréstimo  \n5- Devolução \n6- Estatística do acervo \n7- Remover            (aposenta livros do acervo) \n0- Saida\n\n"))
while opt != 0:
    if opt == 1:
        cadastrar()
    elif opt == 2:
        listar()
    elif opt == 3:
        arg = input("Termo para consulta: \n ")
        consultar(arg)
    elif opt == 4:
        id = int(input("Livro para retirar, informe o id: "))
        saida(id)
    elif opt == 5:
       id = int(input("Livro para devolução, informe o id: "))
       entrada(id)
    elif opt == 6:
        relatorio()
    elif opt == 7: 
        id = int(input("Para remover livro do acervo, informe o id: "))
        delete(id)
    opt = int(input("\nSelecione a opção desejada: \n1- Cadastrar          (para incluir livros novos) \n2- Listar             (lista todo o acervo) \n3- Consulta           (consulta em título, autor ou assunto) \n4- Empréstimo  \n5- Devolução \n6- Estatística do acervo \n7- Remover            (aposenta livros do acervo) \n0- Saida\n\n"))
print("Bye")
            