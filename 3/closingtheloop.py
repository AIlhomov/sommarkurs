n = int(input())

for t in range(n):
    s = int(input())

    l = list(map(str, input().split()))
    
    blue = []
    red = []
    for segment in l:
        if segment.endswith('B'): #blue
            segment = int(segment.removesuffix('B'))
            blue.append(segment)
        else:
            segment = int(segment.removesuffix('R'))
            red.append(segment)
    #print(blue, red)
    #take longest rope first.
    blue.sort(reverse=True)
    red.sort(reverse=True)
    pairs = min(len(blue), len(red))
    res = 0
    #print(pairs)
    if pairs == 0:
        res = 0
    else:
        for i in range(pairs):
            res += blue[i] + red[i] - 2 #knot
    print(f'Case #{t+1}:', int(res))