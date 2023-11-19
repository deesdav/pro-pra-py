def listsindict(a,b,c):
    dict = {}

    for i in [a,b,c]:
        for j in i:
            if j[0] in dict:
                dict[j[0]].append(j[1])
            else:
                dict[j[0]] = [0,0]
                dict[j[0]][0] = j[1]

    print(dict)
    return a,b,c

listsindict([(1,2), (4,3), (5,1)], [(1,3), (2,4), (5,2)], [(2,5), (4,1), (10,1)])
