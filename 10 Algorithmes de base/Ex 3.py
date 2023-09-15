def delta(tab: list)->list:
    liste = tab[0]
    if tab == []:
        return None
    for indice in range(len(tab)):
        liste.append(tab[indice] - tab[indice - 1])
    return liste
    

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3], "Le premier test n'est pas validé"
assert delta([42]) == [42], "Le deuxième test n'est pas validé"
assert delta([]) == None, "Le troisième test n'est pas validé"