def occurence_lettres(phrase: str) -> dict:
    dico = {}
    for lettre in phrase:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1
    return dico