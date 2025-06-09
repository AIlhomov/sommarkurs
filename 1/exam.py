k = int(input())
s1 = input()
s2 = input()

same = sum(1 for a, b in zip(s1, s2) if a == b)
diff = len(s1) - same

max_score = 0
for x in range(max(0, k - diff), min(k, same) + 1):
    score = 2 * x + diff - k
    res = max(max_score, score)

print(res)