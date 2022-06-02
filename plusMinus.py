def plusMinus(arr):
    positive = negative = zero =  0
    lenght = len(arr)
    for x in arr:
        if x > 0: positive += 1
        elif x < 0: negative += 1
        else: zero += 1
    positive = positive / lenght
    negative = negative / lenght
    zero = zero / lenght
    print(f'''{positive:.6f}
{negative:.6f}
{zero:.6f}''')


plusMinus([1, 1, 0, -1, -1])