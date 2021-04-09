import numpy as np


def verif_queen(position_ligne, position_colonne, array):
    if array[position_ligne + 1,  position_colonne + 1] != 1 and array[position_ligne + 1, position_colonne] != 1 and array[position_ligne - 1, position_colonne] != 1 and array[position_ligne,  position_colonne - 1] != 1 and array[position_ligne,  position_colonne + 1] != 1 and array[position_ligne - 1,  position_colonne - 1] != 1:
        return 1
    else:
        return 0

def ft_eight_queens_puzzle():
    ligne = 8
    colonne = 8
    a = np.zeros((ligne,colonne))
    for i in range(ligne - 1):
        for j in range(colonne - 1):
            if a[i,j] == 0:
                a[i,j] = verif_queen(i, j, a)

    print(a)
ft_eight_queens_puzzle()
