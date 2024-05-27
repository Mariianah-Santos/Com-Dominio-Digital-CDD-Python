import random

def print_board(grid):
    for i in range(0, 9, 3):
        print(f"{grid[i]} {grid[i+1]} {grid[i+2]}")
    print()

def check_winner(grid, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for pos in win_positions:
        if all(grid[p] == player for p in pos):
            return True
    return False

def get_valid_user_move(grid):
    while True:
        try:
            move = int(input("Qual posição você quer jogar? (1-9) => "))
            if move < 1 or move > 9:
                print("Por favor escolha um número entre 1 e 9.")
            elif grid[move - 1] != "_":
                print("Posição já preenchida. Escolha outra!")
            else:
                return move - 1
        except ValueError:
            print("Entrada inválida. Por favor escolha um número entre 1 e 9.")

def get_valid_npc_move(grid):
    while True:
        move = random.randint(1, 9) - 1
        if grid[move] == "_":
            return move

def main():
    print("-=-" * 10)
    print("        Jogo da Velha")
    print("-=-" * 10)
    print("Você pode escolher uma posição de 1 a 9")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    print()

    grid = ["_"] * 9
    print_board(grid)
    

    for turn in range(9):
        if turn % 2 == 0:  # User's turn
            move = get_valid_user_move(grid)
            grid[move] = "X"
        else:  # NPC's turn
            move = get_valid_npc_move(grid)
            grid[move] = "O"
        
        print_board(grid)
        
        if turn >= 4:  # Check for a winner from the 5th move onwards
            if check_winner(grid, "X"):
                print("Parabéns! Você ganhou!!")
                return
            elif check_winner(grid, "O"):
                print("Você perdeu. NPC ganhou!!")
                return

    print("Deu velha. Ninguém venceu!!")

if __name__ == "__main__":
    main()