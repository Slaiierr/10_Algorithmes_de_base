def recherche(tab: list)-> list:
    new_tab = []
    for indice in range(len(tab)):
        if tab[indice - 1] + 1 == tab[indice]:
            new_tab.append((tab[indice - 1], tab[indice]))
    return new_tab

assert recherche([1, 4, 3, 5]) == [], "Ce n'est pas la bonne réponse ! 1"
assert recherche([1, 4, 5, 3]) == [(4,5)], "Ce n'est pas la bonne réponse ! 2"
assert recherche([7, 1, 2, 5, 3, 4]) == [(1,2), (3,4)], "Ce n'est pas la bonne réponse ! 3"
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1,2), (2,3), (-5,-4)], "Ce n'est pas la bonne réponse ! 4"