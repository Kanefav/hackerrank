def birthday(s, d, m):
    if len(s) == 1: 
        if d == s[0]: return 1
    output = 0
    i1 = -1
    i2 = m -1
    for index in range(0, len(s)):
        soma = 0
        i1 += 1
        i2 += 1
        if i2 > len(s): break
        for num in range(i1, i2):
            soma += s[num]
        if soma == d: output += 1
    return output 
            


print(birthday([1, 2, 1, 3, 2], 3, 2))