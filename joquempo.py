import os
import time
import random
import socket

class Joquempo:
    def __init__(self) -> None:
        # Cores:
        self.RED, self.GREEN, self.YELLOW, self.BLUE, self.MAGENTA, self.WHITE, self.GRAY, self.CYAN, self.BOLD = ("\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[97m", "\033[90m", "\033[96m", "\033[1m")
        # Estilo Negrito:
        self.BOLD = "\033[1m"
        # Resetando configurações de estilo:
        self.RESET = "\033[0m"
        # Ambiente do Jogo:
        self.elements = {1:'Pedra', 2:'Papel', 3:'Tesoura'}
        self.power = {1:3, 2:1, 3:2}
        # self.score = {"rounds":int, self.player:int, self.machine_name:int, moves:{}}
        self.score = {}
        ## Pegando o nome da máquina:
        self.machine_name = socket.gethostname()
        self.machine_message = (
            f"{self.RED}👾 Saudações, humano!\n"
            "\n"
            "\tVocê está prestes a enfrentar a maior inteligência artificial de Pedra, Papel\n\te Tesoura já criada...\n"
            f"\n\tMe chamo {self.GREEN}{self.machine_name}{self.RED}, o campeão invicto dos circuitos!\n"
            "\n"
            "\tVocê ousa me desafiar? Espero que esteja preparado para a derrota!\n"
            "\n"
            "\tMas antes de começarmos, diga-me...\n"
            "\tQual é o seu nome, corajoso desafiante?\n"
            f"{self.RESET}"
        )
    
    def __type_message(self, message:str, delay:float = 0.03) -> None:
        # Simulando digitação letra a letra:
        for char in message:
            # Printa um unico caractere da mensagem e não pula linha
            print(char, end="", flush=True)
            # Marca um delay entre uma letra e outra, dando efeito de digitação
            time.sleep(delay)
    def __score(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.CYAN}=" * 80)
        print(" " * 42 + "PLACAR FINAL")
        print("=" * 80)

        print(f"\nRodadas Jogadas: {self.score['rounds']}\n")

        print("🏆 Resultados:")
        for player in self.score:
            if player not in ("rounds", "moves"):
                print(f"    {player:<10}: {self.score[player]} vitória(s)")
        print("\n🎯 Movimentos por rodada:\n")
        rounds = self.score["rounds"]
        for i in range(rounds):
            player_move = self.score["moves"][self.player][i]
            machine_move = self.score["moves"][self.machine_name][i]
            print(f"    Rodada {i + 1}: {self.player} jogou {player_move:<8} | {self.machine_name} jogou {machine_move}")
        print("\n" + "=" * 80 + f"{self.RESET}")

    def main(self) -> None:
        playing = True
        rounds = 1
        draw = player = machine = 0
        self.__type_message(self.machine_message)
        self.player = input(f"{self.MAGENTA}\n 👤 Seu nome: {self.WHITE}").strip()
        self.__type_message(f"{self.RED}\n\tBem vindo, {self.MAGENTA}HUMANO!{self.RED} Que comecem os Jogos!\n{self.RESET}")
        moves = {self.player:[], self.machine_name:[]}
        time.sleep(1)
        while playing:
            self.__type_message(f"{self.BOLD}{self.BLUE}\n\t Faça sua Escolha:\n\t 1 - Pedra\n\t 2 - Papel\n\t 3 - Tesoura \n")
            try:
                player_move = int(input(f"\n\tDigite apenas um número [1|2|3]: {self.RESET}"))
                if player_move not in (1,2,3):
                    raise ValueError(f"\n\n⛔ Movimento inválido! Escolha 1 (Pedra), 2 (Papel) ou 3 (Tesoura).\n\n")
                else:
                    machine_move = random.choice((1,2,3))
                    if player_move == machine_move:
                        draw += 1
                        self.__type_message(f"{self.YELLOW}\n\tEmpate entre {self.player} e {self.machine_name}, pois {self.elements[player_move]} é igual a {self.elements[machine_move]}")
                    elif self.power[player_move] == machine_move:
                        player += 1
                        self.__type_message(f"{self.YELLOW}\n\t Vitória de {self.player}, pois {self.elements[player_move]} mata {self.elements[machine_move]}")
                    else:
                        machine += 1
                        self.__type_message(f"{self.YELLOW}\n\t Vitória de {self.machine_name}, pois {self.elements[machine_move]} mata {self.elements[player_move]}")
                    moves[self.player].append(self.elements[player_move])
                    moves[self.machine_name].append(self.elements[machine_move])
                    self.score["rounds"], self.score[self.player], self.score[self.machine_name], self.score["moves"] = (rounds, player, machine, moves)
                    continue_game = input(f"{self.RED}\n\n\tPrecione a tecla {self.CYAN}**ENTER**{self.RED} se deseja jogar mais uma vez ou {self.CYAN}**N**{self.RED} para finalizar. {self.RESET}" ).strip()
                    if continue_game != '':
                        self.__score()
                        playing = False
                    else:
                        rounds += 1
                        os.system('cls' if os.name == 'nt' else 'clear')
            except ValueError as e:
                if "invalid literal" in str(e):
                    print(f"{self.GRAY}\n❌ Entrada inválida! Digite um **número** inteiro (1, 2 ou 3).\n")
                else:
                    print(f"{self.GRAY}\n{e}{self.RESET}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    new_game = Joquempo()
    new_game.main()