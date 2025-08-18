import sys
n = int(input())

# small impossible cases
if n in {1, 2, 3, 5, 7, 11}:
    print("impossible")
    sys.exit(0)

# if n is composite, output one factorization (minimum crates = 1)
def composite_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i, n // i   # i >= 2 and (n//i) >= 2
        i += 1
    return None  # prime

fac = composite_factor(n)
if fac:
    a, b = fac
    print(f"{a}x{b}")
    sys.exit(0)

# n is prime and >= 13 --> two crates: 9 + (n-9)
# (n-9) is even and >= 4, so 2 x ((n-9)/2)
a1, b1 = 3, 3
a2, b2 = 2, (n - 9) // 2
print(f"{a1}x{b1} {a2}x{b2}")
