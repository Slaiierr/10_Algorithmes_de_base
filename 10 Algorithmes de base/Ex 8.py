def recherche(elt: int, tab: list)-> int:
    indice_found = -1
    taille = len(tab) - 1
    for indice in range(taille, -1, -1):
        if tab[indice] == elt:
            indice_found = indice
    return indice_found
        

assert recherche(1, [2, 3, 4]) == -1, "Le premier test n'est pas validé"
assert recherche(1, [10, 12, 1, 56]) == 2, "Le deuxième test n'est pas validé"
assert recherche(50, [1, 50, 1]) == 1, "Le troisième test n'est pas validé"
assert recherche(15, [8, 9, 10, 15]) == 3, "Le quatrième test n'est pas validé"


def recherche_new(elt: int, tab: list) -> int:
    occ = -1
    trouve = False
    taille = len(tab)
    indice = 0
    while (not trouve) and (indice < taille):
        if elt == tab[indice]:
            occ = indice
        indice += 1
    return occ

assert recherche_new(1, [2, 3, 4]) == -1, "Le premier test n'est pas validé"
assert recherche_new(1, [10, 12, 1, 56]) == 2, "Le deuxième test n'est pas validé"
assert recherche_new(50, [1, 50, 1]) == 1, "Le troisième test n'est pas validé"
assert recherche_new(15, [8, 9, 10, 15]) == 3, "Le quatrième test n'est pas validé"