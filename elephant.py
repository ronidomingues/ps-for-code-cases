import os

def elephant() -> None:
    try:
        match_numb = input("Digite o número de elefantes presentes: ")
        if match_numb:
            repetitions = int(match_numb)
            music = f"Um elefante incomoda muita gente!\n"
            if repetitions > 1:
                for numb in range(2, repetitions + 1):
                    music += f"{numb} elefantes " + "incomodam "*numb + "muito mais!\n"
                    if repetitions > numb:
                        music += f"{numb} elefantes incomodam muita gente!\n"
                print(music)
            else:
                print(music)
        else:
            raise ValueError("String vazia! Nada a converter para inteiro!")
    except ValueError as e:
        print(e)
        elephant()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    elephant()