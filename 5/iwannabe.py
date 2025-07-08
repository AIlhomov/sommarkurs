n, k = map(int, input().split())

l = {}

for i in range(n):
    a, d, h = map(int, input().split())

    l[i] = (a, d, h)

#l = sorted(l.items(), key = lambda item : item[1], reverse=True)

ultimate = set()

topAttack = sorted(l.items(), key = lambda item : item[1][0], reverse=True)[:k]
ultimate.update(a[0] for a in topAttack)

topDefense = sorted(l.items(), key = lambda item : item[1][1], reverse=True)[:k]
ultimate.update(a[0] for a in topDefense)

topHealth = sorted(l.items(), key = lambda item : item[1][2], reverse=True)[:k]
ultimate.update(a[0] for a in topHealth)

print(len(ultimate))