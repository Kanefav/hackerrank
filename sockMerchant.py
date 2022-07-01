def sockMerchant(n, ar):
    socks_set = set()
    for s in range(0, n):
        socks_set.add(ar[s])
    socks = list(socks_set)
    output = 0
    for sock in range(0, len(socks)):
        temp = ar.count(socks[sock])
        if temp > 1:
            output += temp // 2
    return output
            
    
print(sockMerchant(6, [10, 10, 20, 10, 20, 20]))