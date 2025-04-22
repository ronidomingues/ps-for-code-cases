def elefantar():
    limite = int(input('Digite o número de elefantes presentes: '))
    if (limite < 1):
        print('Eu sei que há pelo menos um elefante. Não minta para mim.')
        elefantar()
    n = 1
    if limite == 1:
        print('Um elefante incomoda muita gente')
        
    else:
        limite = limite - 1
        while (n <= limite):
            if (n == 1):
                print('Um elefante incomoda muita gente')
                print('2 elefantes incomodam incomodam muito mais!')
                n += 1
            else:
                print(f'{n} elefantes incomodam muita gente')
                n += 1               
                print(f'{n} elefantes {n * "incomodam "}muito mais!')            
if __name__ == "__main__":
    elefantar()