#Alunos: Carlos Eduardo Wille Martins, Raul Castelnou, Wlademir Alves de Souza

import random
import getpass
from colorama import Style, Fore

# Define estilos e cores para facilitar a leitura
reset = Style.RESET_ALL
vermelho = Fore.RED
azul = Fore.BLUE
verde = Fore.GREEN
amarelo = Fore.YELLOW

# Início do programa
while True:
    # Menu principal
    print("[1] Jogador x Jogador")
    print("[2] Jogador x Máquina")
    print("[3] Máquina x Máquina")
    print(f"{vermelho}[4] Sair{reset}")
    opcao = input("Digite a opção desejada: ")

    # Jogador contra Jogador
    if opcao == "1":
        jogador1_vitorias = 0
        jogador2_vitorias = 0
        empates = 0

        while True:
            print("Jogador x Jogador")
            print("Jogador 1 - Escolha o que vai jogar:")
            print("[1] ✊ (pedra)")
            print("[2] ✋ (papel)")
            print("[3] ✌️ (tesoura)")

            opcao_jogador1 = getpass.getpass("Jogador 1 - O que deseja jogar? ")

            if opcao_jogador1 == "1":
                jogador1 = "pedra"
            elif opcao_jogador1 == "2":
                jogador1 = "papel"
            elif opcao_jogador1 == "3":
                jogador1 = "tesoura"
            else:
                print(f"{vermelho}Opção inválida!{reset}")
                continue

            print("Jogador 2 - Escolha o que vai jogar:")
            print("[1] ✊ (pedra)")
            print("[2] ✋ (papel)")
            print("[3] ✌️ (tesoura)")

            opcao_jogador2 = getpass.getpass("Jogador 2 - O que deseja jogar? ")

            if opcao_jogador2 == "1":
                jogador2 = "pedra"
            elif opcao_jogador2 == "2":
                jogador2 = "papel"
            elif opcao_jogador2 == "3":
                jogador2 = "tesoura"
            else:
                print(f"{vermelho}Opção inválida!{reset}")
                continue

            print(f"Jogador 1: {jogador1} - Jogador 2: {jogador2}")

            if jogador1 == jogador2:
                empates += 1
                print(f"{amarelo}***********************")
                print("Empate!")
                print(f"***********************{reset}")
            elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
                 (jogador1 == "papel" and jogador2 == "pedra") or \
                 (jogador1 == "tesoura" and jogador2 == "papel"):
                jogador1_vitorias += 1
                print(f"{verde}***********************")
                print("Jogador 1 ganhou!")
                print(f"***********************{reset}")
            else:
                jogador2_vitorias += 1
                print(f"{azul}***********************")
                print("Jogador 2 ganhou!")
                print(f"***********************{reset}")

            print(f"{amarelo}Placar: Jogador 1 = {jogador1_vitorias}, Jogador 2 = {jogador2_vitorias}, Empates = {empates}{reset}")
            print(f"[1] Continuar - {vermelho}[2] Sair{reset}")
            continuar = input("Digite a opção desejada: ")
            if continuar == "1":
                continue
            elif continuar == "2":
                break
            else:
                print("Opção invalida")


    # Jogador contra Máquina
    elif opcao == "2":
        jogador_vitorias = 0
        maquina_vitorias = 0
        empates = 0

        while True:
            print("Jogador x Máquina")
            print("[1] ✊ (pedra)")
            print("[2] ✋ (papel)")
            print("[3] ✌️ (tesoura)")

            opcao_jogador = input("O que deseja jogar? ")

            if opcao_jogador == "1":
                jogador = "pedra"
            elif opcao_jogador == "2":
                jogador = "papel"
            elif opcao_jogador == "3":
                jogador = "tesoura"
            else:
                print(f"{vermelho}Opção inválida!{reset}")
                continue

            print("Máquina está pensando...")
            opcao_maquina = random.randint(1, 3)

            if opcao_maquina == 1:
                maquina = "pedra"
            elif opcao_maquina == 2:
                maquina = "papel"
            elif opcao_maquina == 3:
                maquina = "tesoura"

            print(f"Você jogou: {jogador}")
            print(f"A máquina jogou: {maquina}")

            if jogador == maquina:
                empates += 1
                print(f"{amarelo}***********************")
                print("Empate!")
                print(f"***********************{reset}")
            elif (jogador == "pedra" and maquina == "tesoura") or \
                 (jogador == "papel" and maquina == "pedra") or \
                 (jogador == "tesoura" and maquina == "papel"):
                jogador_vitorias += 1
                print(f"{verde}***********************")
                print("Você ganhou!")
                print(f"***********************{reset}")
            else:
                maquina_vitorias += 1
                print(f"{vermelho}***********************")
                print("Você perdeu!")
                print(f"***********************{reset}")

            print(f"{amarelo}Placar: Jogador = {jogador_vitorias}, Máquina = {maquina_vitorias}, Empates = {empates}{reset}")
            print(f"[1] Continuar - {vermelho}[2] Sair{reset}")
            continuar = input("Digite a opção desejada: ")
            if continuar == "1":
                continue
            elif continuar == "2":
                break
            else:
                print("Opção invalida")


    # Máquina contra Máquina
    elif opcao == "3":
        maquina1_vitorias = 0
        maquina2_vitorias = 0
        empates = 0

        while True:
            print("Máquina x Máquina")

            opcao_maquina1 = random.randint(1, 3)
            opcao_maquina2 = random.randint(1, 3)

            if opcao_maquina1 == 1:
                maquina1 = "pedra"
            elif opcao_maquina1 == 2:
                maquina1 = "papel"
            elif opcao_maquina1 == 3:
                maquina1 = "tesoura"

            if opcao_maquina2 == 1:
                maquina2 = "pedra"
            elif opcao_maquina2 == 2:
                maquina2 = "papel"
            elif opcao_maquina2 == 3:
                maquina2 = "tesoura"

            print(f"{verde}Máquina 1 jogou: {maquina1}{reset}")
            print(f"{azul}Máquina 2 jogou: {maquina2}{reset}")

            if maquina1 == maquina2:
                empates += 1
                print(f"{amarelo}***********************")
                print("Empate!")
                print(f"***********************{reset}")
            elif (maquina1 == "pedra" and maquina2 == "tesoura") or \
                 (maquina1 == "papel" and maquina2 == "pedra") or \
                 (maquina1 == "tesoura" and maquina2 == "papel"):
                maquina1_vitorias += 1
                print(f"{verde}***********************")
                print("Máquina 1 ganhou!")
                print(f"***********************{reset}")
            else:
                maquina2_vitorias += 1
                print(f"{azul}***********************")
                print("Máquina 2 ganhou!")
                print(f"***********************{reset}")

            print(f"{amarelo}Placar: Máquina 1 = {maquina1_vitorias}, Máquina 2 = {maquina2_vitorias}, Empates = {empates}{reset}")
            print(f"[1] Continuar - {vermelho}[2] Sair{reset}")
            continuar = input("Digite a opção desejada: ")
            if continuar == "1":
                continue
            elif continuar == "2":
                break
            else:
                print("Opção invalida")

    # Sair do jogo
    elif opcao == "4":
        print(f"{vermelho}Finalizando o programa!{reset}")
        break

    # Opção inválida no menu principal
    else:
        print(f"{vermelho}Opção inválida!{reset}")
