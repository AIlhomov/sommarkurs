import heapq

def dijkstra(graph, source):
    n = len(graph) - 1 # 1 indexed
    dist = [float('inf')] * (n + 1)
    dist[source] = 0
    visited = [False] * (n + 1)

    heap = [(0, source)] # (dist, node)

    while heap:
        curr_dist, u = heapq.heappop(heap)

        if visited[u]:
            continue
        visited[u] = True

        for v, weight in graph[u]:
            new_dist = curr_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist

attack, health = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    e, b, enemyAttack, enemyHealth = map(int, input().split())

    rounds = (enemyHealth + attack - 1) // attack
    hits = max(0, rounds - 1)
    cost = hits * enemyAttack

    graph[e].append((b, cost))

    #graph[(e, b)] = (enemyAttack, enemyHealth)

path = dijkstra(graph, 1)
minDamage = path[n]

if minDamage == float('inf') or minDamage >= health:
    print('Oh no')
else:
    print(health - minDamage)