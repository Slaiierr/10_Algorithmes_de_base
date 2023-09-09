def calcul(n: int)-> list:
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            liste.append(n)
        else:
            n = n * 3 + 1
            liste.append(n)
    return liste

assert calcul(7) == [7, 22, 11 , 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "Le résultat n'est pas correct"