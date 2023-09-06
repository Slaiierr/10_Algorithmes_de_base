def occurence_lettres(phrase: str)-> dict:
    dico = {}
    for lettre in phrase:        
        if dico[lettre] == False:
            dico[lettre] = 1
        if dico[lettre] == True:
            dico[lettre] += 1
    return dico

assert occurence_lettres('Hello world !') == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}, "La réponse est fausse !"