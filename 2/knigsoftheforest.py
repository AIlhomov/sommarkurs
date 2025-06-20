import heapq

k, n = map(int, input().split())

#y = year of entry into the tournament and p = his strength
y, p = map(int, input().split()) #Karl-Älgtav

moose = []

# moose_years = []
# moose_strength = []

for i in range(n+k-2):
    a, b = map(int, input().split())
    
    moose.append((a, b))

moose.append((y, p)) #add the konung ofc
moose.sort(key=lambda x: x[0]) #sort by year.

moose_by_year = {}
for key, val in moose: #key = year, val = strength
    if key not in moose_by_year:
        moose_by_year[key] = []
    moose_by_year[key].append((key, val))


curr_pool = []
heapq.heapify(curr_pool)

for year in sorted(moose_by_year.keys()):
    for moose_entry in moose_by_year[year]:
        heapq.heappush(curr_pool, (-moose_entry[1], moose_entry[0]))  # negative strength for max-heap behavior

    alpha = heapq.heappop(curr_pool)  # strongest moose in the current pool
    if (-alpha[0], alpha[1]) == (p, y):
        print(year)
        break
else:
    print("unknown")

