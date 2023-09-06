def maxi(tab: list)-> tuple:
    elt_max = tab[0]
    indice_max = tab[0]
    for elt in tab:
        if elt >= elt_max:
            elt_max = tab[elt]
            indice_max = tab[elt]
        