import random
print("-=-"*10)
print("        Jogo da Velha")
print("-=-"*10)
print("VOCE PODE ESCOLHER ATE A POSIÇÃO D 1 AO 9")
print("1 2 3")
print("4 5 6")
print("7 8 9")
grid = ["_"]*9 # tupla criada para receber as entradas do usuario
turno = 0
def tela(grid): # função criada para mostra as linhas e colunas
    for indice in range(len(grid)):
        print(grid[indice], end=" ")
        if indice == 2 or indice == 5: # toda vez que a posição(indice) estive no indece 2 ou 5 pula uma linha
            print(" ") 
def verificarGrid(grid, player): # Verificar se ganhou 
    # verificando se ganhou por linha
    if grid[0] == player and grid[1] == player and grid[2] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[3] == player and grid[4] == player and grid[5] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[6] == player and grid[7] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2

    # verificando se ganhou por coluna
    if grid[0] == player and grid[3] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[1] == player and grid[4] == player and grid[7] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[5] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2

    # verificando se ganhou na diagonal 
    if grid[0] == player and grid[4] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[4] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    return 0 
while True: # Laço para repetição 
    escolha_usuario = int(input("Qual Posição você jogar? => ")) # escolha do usuario
    npc = random.randint(1, 9) # escolha do pc
    while grid[escolha_usuario - 1] != "_": # Se o usuario escolhe uma posição já preenchida, ele pede para escolhe outra
        print("Posição já foi preenchida. Por favor escolha outra!!")
        escolha_usuario = int(input("Qual Posição você jogar? => "))

    grid[escolha_usuario - 1] = "X" # irá colocar a entrada do usuario em uma das posições (irá subtituir o _ por 'x' ou 'o')
    turno += 1
    vencedor = verificarGrid(grid, "X")
    if vencedor != 0:
        break
    
    while grid[npc - 1] != "_": # Se o pc escolhe uma posição já preenchida, ele pede para escolhe outra
        npc = random.randint(1, 9)
        grid[npc - 1] = "O"

    grid[npc - 1] = "O"
    turno += 1
    vencedor = verificarGrid(grid, "O")
    if vencedor != 0:
        break
    if turno == 9:
        break
    tela(grid)
def ganhado(grid, vencedor):
    if vencedor == 1:
        print("Parabéns você ganhou!!")
        tela(grid)
    elif vencedor == 2:
        print("Você perdeu. NPC ganhou!!")
        tela(grid)
    else:
        print("Deu velha. Ninguém venceu!!")
        tela(grid)
ganhado(grid, vencedor)