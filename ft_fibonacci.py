def ft_fibonacci(index): 
    resultat = 1 
    if index > 2:
        resultat = ft_fibonacci(index -1) + ft_fibonacci(index-2)
    elif index == 0:
        return 0
    return resultat
print(ft_fibonacci(13))
