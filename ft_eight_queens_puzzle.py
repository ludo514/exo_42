import numpy as np

def verif(position_ligne, position_colonne, array):
    compte_colonne = 7 - position_colonne
    compte_ligne = 7 - position_ligne
    for i in range(compte_ligne):
        for j in range(compte_colonne):
            if array[position_ligne, position_colonne - j] != 1 and array[position_ligne + i, position_colonne + j] != 1:
                array[position_ligne, position_colonne] = 1
            else:
                array[position_ligne, position_colonne] = 0

def ft_eight_queens_puzzle():
    ligne = 8
    colonne = 8
    a = np.zeros((ligne,colonne))
    for i in range(ligne - 1):
        for j in range(colonne - 1):
            verif(i, j, a)

    print(a)
ft_eight_queens_puzzle()
