def ft_iterative_power(nombre, puissance):
    resultat = 0
    for i in range(puissance):
        resultat = nombre * nombre
    return resultat


print(ft_iterative_power(3,2))
