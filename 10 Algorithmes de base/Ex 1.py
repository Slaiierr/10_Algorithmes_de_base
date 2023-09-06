def recherche(caractere: str, mot:str)-> int:
    total = 0
    for lettre in mot:
        if lettre == caractere:
            total += 1
    return total

assert recherche('e', 'sciences') == 2, "Recherche n'est pas égal à 2"
assert recherche('i', 'mississipi') == 4, "Recherche n'est pas égal à 4"
assert recherche('m', 'mississipi') == 1, "Recherche n'est pas égal à 1"