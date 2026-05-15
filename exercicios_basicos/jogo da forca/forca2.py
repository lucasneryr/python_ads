import random

linha = "=" * 45
todas_as_respostas = set()
vitoria = False
tentativas = 6
configurado = False

def imprimir_resposta():
    print(linha)
    for letra_palavra in palavra:
        acertou = False
        for letra_resposta in todas_as_respostas:
            if letra_resposta == letra_palavra:
                print(f"{letra_resposta} ", end="")
                acertou = True
        if not acertou:
            print("_ ", end="")
    print("\n")

def verificar_vitoria():
     global vitoria
     if conjunto_palavra - todas_as_respostas == set():
        print("Vitória!")
        vitoria = True

def verificar_se_acertou(resposta):
    print(linha)
    global tentativas
    if resposta in palavra:
        pass
    else:
        print("Errou!!!")
        tentativas -= 1
    print(f"Tentativas: {tentativas}")

while configurado == False:
    print(f"{linha}\nMENU DE NAVEGAÇÃO\n{linha}")
    print ("1. INSERIR A PALAVRA\n")
    print ("2. UTILIZAR PALAVRA ALEATÓRIA\n")
    opcao_menu = int(input("\nSelecione sua opção: "))

    if opcao_menu == 1:
        palavra = input("Escreva sua palavra: ")
        conjunto_palavra = set(palavra)
        configurado = True
    elif opcao_menu == 2:
        print(f"{linha}\nSELECIONE SUA DIFICULDADE\n{linha}")
        print ("1. FÁCIL\n")
        print ("2. MÉDIO\n")
        print ("3. DIFÍCIL\n")
        print ("4. Voltar\n")
        opcao_dificuldade = int(input("\nSelecione a dificuldade: "))
        if opcao_dificuldade > 4 or opcao_dificuldade < 1:
            print("OPÇÃO INVALIDA\n")
        elif opcao_dificuldade == 4:
            pass
        else:
            from banco_palavras import selecionar_palavra
            palavra_aleatoria = selecionar_palavra(opcao_dificuldade) 
            palavra = palavra_aleatoria
            conjunto_palavra = set(palavra)
            configurado = True

while tentativas > 0:
    if vitoria == True:
        break
    imprimir_resposta()
    resposta = input ("insira a letra: ")
    verificar_se_acertou(resposta)
    todas_as_respostas.add(resposta)
    verificar_vitoria()


