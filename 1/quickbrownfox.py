letters = "abcdefghijklmnopqrstuvwxyz"
seen = set()
allLetters = set(letters)

n = int(input())

for i in range(n):
    s = input().lower()

    for c in s:
        if c in letters:
            seen.add(c)

    if len(seen) == len(letters):
        print("pangram")
    else:
        print("missing", "".join(allLetters - seen))
    
    seen.clear()