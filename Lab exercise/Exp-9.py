from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = range(1, n)
min_cost = float('inf')
best_path = None

for route in permutations(cities):
    path = (0,) + route + (0,)
    cost = sum(
        graph[path[i]][path[i + 1]]
        for i in range(n)
    )

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Shortest path:", best_path)
print("Minimum cost:", min_cost)
