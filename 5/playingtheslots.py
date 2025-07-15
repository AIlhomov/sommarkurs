import math

def minHeight(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    numerator = abs((x2 - x1)*(y1 - y3) - (x1 - x3)*(y2 - y1)) # 2D cross product
    denominator = math.hypot(x2 - x1, y2 - y1) # stable instead of sqrt
    return numerator / denominator #height

n = int(input())
poly_coin = []

for i in range(n):
    x, y = map(float, input().split())
    poly_coin.append((x, y))
    
res = float('inf') #biiiig

for i in range(n):
    a = poly_coin[i]
    b = poly_coin[(i + 1) % n]  # wrap around (goes to the first)

    max_height_on_this_edge = 0

    for j in range(n):
        if j == i or j == (i + 1) % n: #not relevant
            continue
        c = poly_coin[j]
        h = minHeight(a, b, c)
        max_height_on_this_edge = max(max_height_on_this_edge, h)

    res = min(res, max_height_on_this_edge)

print(f"{res:.8f}")
