def recherche(elt: int, tab: list)-> int:
    for indice in range(len(tab)):
        if tab[indice] == elt:
            return indice
    return -1
        

assert recherche(1, [2, 3, 4]) == -1, "Le premier test n'est pas validé"
assert recherche(1, [10, 12, 1, 56]) == 2, "Le deuxième test n'est pas validé"
assert recherche(50, [1, 50, 1]) == 1, "Le troisième test n'est pas validé"
assert recherche(15, [8, 9, 10, 15]) == 3, "Le quatrième test n'est pas validé"