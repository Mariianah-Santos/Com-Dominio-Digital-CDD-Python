class Jogo():
    def __init__(self):
        self.grid = ["_"] * 9
        self.jogador_1 = "X"
        self.jogador_2 = "O"

    def telaGrid(self): # crição da do tabuleiro
        for indice in range(len(self.grid)):
            print(self.grid[indice], end=" ")
            if indice == 2 or indice == 5:
                print()

    def jokenpo(self): # jogo
        for turno in range(9): # alterna sobre os jogadores
            if turno % 2 == 0:
                jogador = self.jogador_1
            else:
                jogador = self.jogador_2
            
            jogada = int(input(f"\nJOGADOR {jogador}º ESCOLHA UMA POSIÇÃO DE 1 A 9 => ")) - 1
            if self.grid[jogada] == "_":
                self.grid[jogada] = jogador
                self.telaGrid()
            else:
                while self.grid[jogada] != "_":
                    print("POSIÇÃO JÁ PREENCHIDA. POR FAVOR ESCOLHA OUTRA POSIÇÃO!!")
                    jogada = int(input(f"\nJOGADOR {jogador}º ESCOLHA UMA POSIÇÃO DE 1 A 9 => ")) - 1
                self.grid[jogada] = jogador
                self.telaGrid()
            
            if ((self.grid[0] == self.grid[1] == self.grid[2] == jogador) or
                (self.grid[3] == self.grid[4] == self.grid[5] == jogador) or
                (self.grid[6] == self.grid[7] == self.grid[8] == jogador)):
                print(f"\nJOGADOR [{jogador}] GANHOU JOGANDO PELA LINHA")
                break
            
            elif ((self.grid[0] == self.grid[3] == self.grid[6] == jogador) or
                (self.grid[1] == self.grid[4] == self.grid[7] == jogador) or
                (self.grid[2] == self.grid[5] == self.grid[8] == jogador)):
                print(f"\nJOGADOR [{jogador}] GANHOU JOGANDO PELA COLUNA")
                break
            elif ((self.grid[0] == self.grid[4] == self.grid[8] == jogador) or
                (self.grid[2] == self.grid[4] == self.grid[6] == jogador)):
                print(f"\nJOGADOR [{jogador}] GANHOU JOGANDO PELA DIAGONAL")
                break
        else:
            print("DEU VELHA!! NINGUÉM GANHOU!!!")

    
jokenpo = Jogo()
jokenpo.telaGrid()
jokenpo.jokenpo()
