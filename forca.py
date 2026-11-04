import os
os.system("cls")

forca = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]


os.system("cls" if os.name == "nt" else "clear")  # limpa a tela (Windows ou Mac/Linux)
print("========== JOGO DA FORCA ==========")
desafiante = input("Nome do Desafiante: ")
competidor = input("Nome do Competidor: ")

continuar = "1"

while continuar == "1":


    os.system("cls" if os.name == "nt" else "clear")
    print("Vez do Desafiante:", desafiante, "(o competidor não pode olhar!)")
    print()

    palavra = input("Palavra chave: ").upper()
    while palavra == "" or not palavra.isalpha():
        print("A palavra deve ter somente letras, sem espaços!")
        palavra = input("Palavra chave: ").upper()

    dicas = []
    for i in range(3):
        dica = input("Dica " + str(i + 1) + ": ")
        dicas.append(dica)

    
    os.system("cls" if os.name == "nt" else "clear")
    print("Vez do Competidor:", competidor)

    letras_certas = []
    letras_erradas = []
    erros = 0
    dicas_usadas = 0
    ganhou = False
    oculta = "*" * len(palavra)  

    while erros < 6 and not ganhou:

        print(forca[erros])
        print("Palavra:", oculta, "(" + str(len(palavra)), "letras)")
        print("Letras erradas:", " ".join(letras_erradas))
        print("Erros:", erros, "de 6  |  Dicas usadas:", dicas_usadas, "de 3")
        print()
        print("1 - Jogar")
        print("2 - Solicitar Dica")
        opcao = input("Escolha uma opção: ")

        
        if opcao == "2":
            if dicas_usadas < 3:
                print()
                print(">>> DICA", dicas_usadas + 1, ":", dicas[dicas_usadas])
                dicas_usadas = dicas_usadas + 1
                print("Agora você é obrigado a arriscar uma letra!")
            else:
                print("Você já usou as 3 dicas! Escolha a opção 1.")
                continue
        elif opcao != "1":
            print("Opção inválida!")
            continue

        
        letra_valida = False
        while not letra_valida:
            letra = input("Digite uma letra: ").upper()
            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas UMA letra!")
            elif letra in letras_certas or letra in letras_erradas:
                print("Você já tentou a letra", letra + "!")
            else:
                letra_valida = True

        
        if letra in palavra:
            letras_certas.append(letra)

            
            oculta = ""
            for l in palavra:
                if l in letras_certas:
                    oculta = oculta + l
                else:
                    oculta = oculta + "*"

            print()
            print("Acertou!", oculta)
        else:
            letras_erradas.append(letra)
            erros = erros + 1
            print()
            print("Erro:", erros)

        
        if "*" not in oculta:
            ganhou = True

    
    print(forca[erros])
    print()
    if ganhou:
        print("PARABÉNS! A palavra era", palavra)
        print(competidor, "GANHOU e", desafiante, "perdeu!")
    else:
        print("Você errou 6 vezes! A palavra era", palavra)
        print(desafiante, "GANHOU e", competidor, "perdeu!")

    
    print()
    print("1 - Jogar novamente")
    print("2 - Sair")
    continuar = input("Escolha uma opção: ")
    while continuar != "1" and continuar != "2":
        print("Opção inválida!")
        continuar = input("Escolha uma opção: ")

print("Obrigado por jogar!")
