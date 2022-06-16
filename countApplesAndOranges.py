def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s = startpoint t = endpoint, of the house 
    # a = apple tree location 
    # b = orange tree location 
    apple_outpt = 0
    orange_outpt = 0
    for apple in range(0, len(apples)):
        temp = apples[apple] + a
        if temp >= s:
            if temp <= t: apple_outpt += 1
    print(apple_outpt)
    for orange in range(0, len(oranges)):
        temp = oranges[orange] + b
        if temp >= s:
            if temp <= t: orange_outpt += 1
    print(orange_outpt)


countApplesAndOranges(7 , 10, 4, 12, [2, 3, -4], [3, -2, -4])