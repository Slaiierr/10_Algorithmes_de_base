def rechercheMinMax(tab: list)-> dict:
    dico = {}
    if tab == []:
        dico['min'] = None
        dico['max'] = None
        return dico
    dico['min'] = tab[0]
    dico['max'] = tab[0]
    for elt in tab:
        if elt < dico['min']:
            dico['min'] = elt
        if elt > dico['max']:
            dico['max'] = elt
    return dico
    


assert rechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}, "Le premier test n'est pas bon"
assert rechercheMinMax([]) == {'min': None, 'max': None}, "Le deuxième test n'est pas bon"