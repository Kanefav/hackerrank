def catAndMouse(x, y, z):
    d1 = x - z
    d2 = y - z
    d = [d1, d2]
    for i in range(0, 2):
        if d[i] <= -1:
            d[i] = d[i] * -1
    if d[0] == d[1]: return 'Mouse C'
    elif d[0] < d[1]: return 'Cat A'
    else: return 'Cat B'
    


print(catAndMouse(2, 5, 4))