def binarySearch(array, x):
    low = 0
    high = len(array) - 1
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return low #key part, its not -1.

n, m = map(int, input().split())

sizes = []
microlitre_colour = []

for i in range(n):
    sizes.append(int(input()))

sizes.sort()

for i in range(m):
    microlitre_colour.append(int(input()))

microlitre_colour.sort()
res = 0

for i in range(m):
    index = binarySearch(sizes, microlitre_colour[i])

    res += sizes[index] - microlitre_colour[i] 

print(res)