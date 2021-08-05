def compareTriplets(a, b):
    alice = bob = 0
    for times in range(0, 3):
        if a[times] == b[times]:
            pass
        if a[times] > b[times]:
            alice += 1
        if a[times] < b[times]:
            bob += 1
    return [alice, bob]
    

a = [1, 2, 3]
b = [3, 2, 1]
compareTriplets(a, b)
#exemplo, return [1, 1]