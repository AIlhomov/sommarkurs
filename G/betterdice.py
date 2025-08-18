import bisect

n = int(input())
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

d1.sort()
d2.sort()

first = sum(bisect.bisect_left(d2, x) for x in d1)
second = sum(bisect.bisect_left(d1, x) for x in d2)

if first > second:
    print('first')
elif first < second:
    print('second')
else:
    print('tie')