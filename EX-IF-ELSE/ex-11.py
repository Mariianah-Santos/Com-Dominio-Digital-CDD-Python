import random
resp = "S"
while resp == "S" or resp == "s":
    while True:
        print("-"*15)
        print("  JOGO JOKEPO")
        print("-"*15)
        opcao_usuario = int(input("[1] - Tesoura \n[2] - Papel \n[3] - Pedra \n=> "))
        npc = random.randint(1, 3)

        if opcao_usuario == 1 and npc == 2:
            print(f"Usuario ganhou com TESOURA [{opcao_usuario}] e NPC perdeu com PAPEL [{npc}]")
            break

        elif opcao_usuario == 1 and npc == 3:
            print(f"Usuario perdeu com TESOURA [{opcao_usuario}] e NPC ganhou com PEDRA [{npc}]")
            break

        elif opcao_usuario == 2 and npc == 1:
            print(f"Usuario perdeu com PAPEL [{opcao_usuario}] e NPC ganhou com TESOURA [{npc}] ")
            break

        elif opcao_usuario == 2 and npc == 3:
            print(f"Usuario ganhou com PAPEL [{opcao_usuario}] e NPC perdeu com PEDRA [{npc}] ")
            break

        elif opcao_usuario == 3 and npc == 1:
            print(f"Usuario ganhou com PEDRA [{opcao_usuario}] e NPC perdeu com TESOURA [{npc}]")
            break

        elif opcao_usuario == 3 and npc == 2:
            print(f"Usuario perdeu com PEDRA [{opcao_usuario}] e NPC ganhou com papel[{npc}]")
            break

        elif npc == opcao_usuario:
            print(f"EMPATE NPC - [{npc}] e USUARIO - [{opcao_usuario}]")
            break
        else:
            print("Por favor digite um numero válido!!")
    resp = input("DESEJA JOGAR NOVAMENTE? [S/N] => ")

print("Saindo...")
