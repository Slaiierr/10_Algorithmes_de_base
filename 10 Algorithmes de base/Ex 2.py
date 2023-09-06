def moyenne(liste: list)-> int:
    note = 0
    somme_coefficient = 0
    for elt in liste:
        somme_coefficient += elt[1]
        note += elt[0] * elt[1]
    note_totale = note/somme_coefficient
    return note_totale

assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5, "La moyenne n'est pas correcte"