def bonAppetit(bill, k, b):
    anna = (sum(bill) - bill[k]) / 2
    if anna == b: print('Bon Appetit')
    else: print(int(b - anna))


print(bonAppetit([2, 4, 6], 2, 6))