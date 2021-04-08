import time

def ft_sqrt(nombre):
    resultat = 0
    try:
        for i in range(nombre):
            resultat = i * i
            if resultat == nombre:
                return i
    except TypeError:
        print("Erreur valeur")

nombre = input("Calculé la racine carré de : ")
valeur = ft_sqrt(int(nombre))
if int(nombre) != None and valeur != None:
    print(valeur)
    print(time.process_time())
