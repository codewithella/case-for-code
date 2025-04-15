from random import choice

def jogo():
    pontos_jogador = 0
    pontos_cpu = 0
    opcoes = ["pedra", "papel", "tesoura"]

    for _ in range(15):
        computador = choice(opcoes)
        jogador = input("Pedra, Papel ou Tesoura?\t").strip().lower()

        if jogador == computador:
            print("Empate!")
        elif jogador == "pedra":
            if computador == "papel":
                print("Você perdeu!", computador.capitalize(), "embrulha", jogador)
                pontos_cpu += 1
            else:
                print("Você venceu!!!", jogador.capitalize(), "esmaga", computador)
                pontos_jogador += 1
        elif jogador == "papel":
            if computador == "tesoura":
                print("Você perdeu!", computador.capitalize(), "corta", jogador)
                pontos_cpu += 1
            else:
                print("Você venceu!!!", jogador.capitalize(), "embrulha", computador)
                pontos_jogador += 1
        elif jogador == "tesoura":
            if computador == "pedra":
                print("Você perdeu...", computador.capitalize(), "esmaga", jogador)
                pontos_cpu += 1
            else:
                print("Você venceu!!", jogador.capitalize(), "corta", computador)
                pontos_jogador += 1
        else:
            print("Essa não é uma jogada válida. Por favor, verifique a ortografia!")

        print(f"\nPlacar --> Pontos do Jogador: {pontos_jogador}; Pontos da Máquina: {pontos_cpu}\n\n")

    # Apenas o placar final
    print(f"Placar Final: Jogador {pontos_jogador} x {pontos_cpu} Máquina")

# Executa o jogo
jogo()
