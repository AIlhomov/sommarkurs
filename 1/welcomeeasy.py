n = int(input())

find = "welcome to code jam"

def solve(s):
    def dp(pos_s, pos_g):
        if pos_g == len(find):
            return 1 # matched ALL
        if pos_s == len(s):
            return 0 # reached end of line without matching all

        tot = dp(pos_s + 1, pos_g)

        if s[pos_s] == find[pos_g]:
            tot += dp(pos_s + 1, pos_g + 1)
        return tot % 10000 # last 4
    return dp(0, 0)

for i in range(1, n+1):
    s = input()

    print(f"Case #{i}: {solve(s):04d}")


