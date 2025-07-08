
memo = {}
# egg dropping
def solvePuzzle(k, a, n):
        
    #base case:
    if k == 1:
        return (n * (n + 1)) // 2 - (a * (a + 1)) // 2
    if k == 0:
        return float('inf')
    if a == n:
        return 0

    if (k, a, n) in memo:
        return memo[(k, a, n)]
    
    minimum = float('inf')

    for i in range(a + 1, n + 1):
        minimum = min(minimum, i + max(solvePuzzle(k - 1, a, i - 1), solvePuzzle(k, i, n)))
    memo[(k, a, n)] = minimum

    return minimum

n = int(input())

for i in range(n):
    k, m = map(int, input().split())

    # k = mailboxes, m = how many each mailbox fits.

    if k == 1:
        print((m*(m+1))//2)
    else:
        print(solvePuzzle(k, 0, m))