import random
grid = ["_"] * 9

def telaGrid(grid): # tela onde vai aparecer os quadradinhos
    for indice in range(len(grid)):
        print(grid[indice], end=" ")
        if indice == 2 or indice == 5:
            print()
def verificandoErrorUsuario(grid): # verificação d erros de entrada do usuario 
    while True:
        try:
            escolha = int(input("\nESCOLHA UMA POSIÇÃO DE 1 A 9 => "))
            if escolha < 1 or escolha > 9:
                print("Por favor digite um número válido! De 1 a 9!!")
                print()
                print("STATUS ATUAL")
                telaGrid(grid)
            elif grid[escolha - 1] != "_":
                print("Posição já preenchida. Por favor escolha outro!!")
                print()
                print("STATUS ATUAL")
                telaGrid(grid)
            else:
                return escolha - 1
        except ValueError:
            print("Valor errado. Por favor Digite números!!")
            print()
            print("STATUS ATUAL")
            telaGrid(grid)
def npcError(grid): # verificação de erro feito pelo npc
    while True:
        npc = random.randint(1, 9) - 1
        if grid[npc] == "_":
            return npc
        
def vencedor(grid, player):
    # verificando se ganhou por linha
    if grid[0] == player and grid[1] == player and grid[2] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    if grid[3] == player and grid[4] == player and grid[5] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    if grid[6] == player and grid[7] == player and grid[8] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    # verificnado se ganhou por coluna
    if grid[0] == player and grid[3] == player and grid[6] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    if grid[1] == player and grid[4] == player and grid[7] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")   
            telaGrid(grid)
        exit() 
    if grid[2] == player and grid[5] == player and grid[8] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    # verificnado se ganhou por diagonal
    if grid[0] == player and grid[4] == player and grid[8] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    if grid[2] == player and grid[4] == player and grid[6] == player:
        if player == "X":
           ganhador = player
           print("VOCÊ GANHOU!! PARABÉNS!!")
           telaGrid(grid)
        elif player == "O":
            ganhador = player
            print("NPC GANHOU!! PARABÉNS")
            telaGrid(grid)
        exit()
    
def menu(): # menu de exibição
    print("-=-" * 10)
    print(" " * 7,"Jogo da Velha")
    print("-=-" * 10)
    print("Você pode escolher uma posição de 1 a 9")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
def jokenpo(): # jogo completo
    
    while True:
        escolha = verificandoErrorUsuario(grid)
        grid[escolha] = "X"
        
        npc = npcError(grid)
        grid[npc] = "O"
        ganhador = vencedor(grid, "X") 
        ganhador = vencedor(grid, "O") 
        telaGrid(grid)
        
menu()        
jokenpo()