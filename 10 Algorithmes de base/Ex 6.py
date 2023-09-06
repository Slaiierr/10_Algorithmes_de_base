def maxi(tab: list)-> tuple:
    elt_max = tab[0]
    indice_max = tab[0]
    for indice in range(len(tab)):
        if tab[indice] > elt_max:
            elt_max = tab[indice]
            indice_max = indice
    return (elt_max,indice_max)

assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9,3), "Le résultat n'est pas correct"

        