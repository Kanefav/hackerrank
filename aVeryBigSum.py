def aVeryBigSum(ar):
    #return sum(ar)
    output = 0
    for num in ar:
        output += num
    return output
        


print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))