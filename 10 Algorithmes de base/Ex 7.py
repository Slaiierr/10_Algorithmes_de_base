def conv_bin(n: int)-> tuple:
    b = []
    bit = 0
    quotient = n
    while quotient != 0:
        b.append(quotient % 2)
        quotient = quotient // 2
        bit += 1
    b.reverse()
    return (b, bit)

assert conv_bin(9) == ([1, 0, 0, 1], 4), "Le test 1 n'est pas validé"
assert conv_bin(2) == ([1, 0], 2), "Le test 2 n'est pas validé"
assert conv_bin(410) == ([1, 1, 0, 0, 1, 1, 0, 1, 0], 9), "Le test 3 n'est pas validé" 
assert conv_bin(11) == ([1, 0, 1, 1], 4), "Le test 3 n'est pas validé" 