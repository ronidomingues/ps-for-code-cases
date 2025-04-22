import random 

def menu():
    print('Bem vindo ao jogo!')
    print('1-Jogar')
    print('2-Sair')
    choicemenu = int(input('Escolha a opção do menu: '))
    if choicemenu == 1:
        Jogar()
    elif choicemenu == 2:
        exit()
    else: 
        menu()

win = 0
lose = 0
draw = 0

def Jogar(): 
    jogando = True
    global win
    global lose
    global draw
    while jogando:
        print('Selecione o que quer jogar:')
        print('1-Pedra')
        print('2-Papel')
        print('3-Tesoura')
        escolhas = ['Pedra', 'Papel', 'Tesoura']
        choiceuser = int(input('Digite o número equivalente ao que quer jogar: '))
        choicebot = random.choice(escolhas)
        print(f'O computador jogou {choicebot}!')
        if (choiceuser != 1 and choiceuser != 2 and choiceuser != 3):
            Jogar()
        elif (choiceuser == 1 and choicebot == 'Pedra') or \
            (choiceuser == 2 and choicebot == 'Papel') or \
            (choiceuser == 3 and choicebot == 'Tesoura'):
            print("\033[33mO jogo empatou!\033[0m")
            draw += 1
        elif (choiceuser == 1 and choicebot == 'Tesoura') or \
            (choiceuser == 2 and choicebot == 'Pedra') or \
            (choiceuser == 3 and choicebot == 'Papel'):
            print("\033[32mVocê venceu!\033[0m")
            win += 1
        else:
            print("\033[31mVocê perdeu...\033[0m")
            lose +=1
        print(f'Placar: {win} vitórias, {draw} empates e {lose} derrotas')
        print('Jogar de novo?')
        dnv = input('Digite "S" para sim ou qualquer outra coisa para não: ')
        if (dnv.upper() != 'S'):
            jogando = False
            print(f'Placar final: {win} vitórias, {draw} empates e {lose} derrotas.')

if __name__ == "__main__":
    menu()