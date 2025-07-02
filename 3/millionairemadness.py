import heapq

def solve(grid):
    n = len(grid)
    m = len(grid[0])
    cost = [[float('inf')] * m for _ in range(n)]
    cost[0][0] = 0
    heap = [(0, 0, 0)]  # (current max diff, row, col)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while heap:
        curr_cost, r, c = heapq.heappop(heap)
        if (r, c) == (n-1, m-1):
            return curr_cost
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                diff = max(0, grid[nr][nc] - grid[r][c]) # cost to next cell
                next_cost = max(curr_cost, diff)
                #print(next_cost)
                if next_cost < cost[nr][nc]:
                    cost[nr][nc] = next_cost
                    heapq.heappush(heap, (next_cost, nr, nc))
    return -1  # unreachable

n, m = map(int, input().split())
vault = []
for i in range(n):
    vault.append(list(map(int, input().split())))

print(solve(vault))
