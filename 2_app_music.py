pesos1 = [9, 3, 2, 5, 5, 19, 20, 1, 2, 2]

def arrumar(pesos):
    pesos.sort(reverse=True)
    n_musicas = len(pesos)
    listafinal = []

    ind_inicio = 0
    ind_fim = n_musicas
    while ind_inicio<=n_musicas/2:
        listafinal.append(pesos[ind_inicio])
        ind_inicio += 1

        if ind_inicio<n_musicas/2:
            ind_fim -= 1
            listafinal.append(pesos[ind_fim])
    print(listafinal)

if __name__ == "__main__":
    arrumar(pesos1)