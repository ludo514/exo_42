def ft_recursive_power(nombre, puissance):
    resultat = nombre * nombre
    if puissance > 0:
        ft_recursive_power(nombre, puissance -1)
    return resultat

print(ft_recursive_power(5,2))
