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
if int(nombre) != None and ft_sqrt(int(nombre)) != None:
    print(ft_sqrt(int(nombre)))
    print(time.process_time())
