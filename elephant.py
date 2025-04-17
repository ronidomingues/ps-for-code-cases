import re
import os

def elephant(message:str = "3 elefantes") -> None:
    try:
        match_numb = re.search(r"\d+", message.strip())
        match_str = re.sub(r"^\d+\s+", "", message.strip())
        if match_numb:
            repetitions = int(match_numb.group())
            music = f"Um {match_str} incomoda muita gente!\n"
            if repetitions > 1:
                for numb in range(2, repetitions + 1):
                    music += f"{numb} {match_str} " + "incomodam "*numb + "muito mais!\n"
                    if repetitions > numb:
                        music += f"{numb} {match_str} incomodam muita gente!\n"
                print(music)
            else:
                print(music)
        else:
            raise ValueError("String vazia! Nada a converter para inteiro!")
    except AttributeError:
        print(" Group não pode ser aplicado em valores nulos(None)")
    except ValueError as e:
        print(e)
    except TypeError:
        print("A mensagem passada não é uma string")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    elephant()