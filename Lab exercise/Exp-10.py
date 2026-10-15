import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_cost = cost + weight
                priority = new_cost + heuristic[neighbour]

                heapq.heappush(
                    queue,
                    (priority, new_cost, neighbour,
                     path + [neighbour])
                )

    return None, float('inf')

path, cost = astar('A', 'D')

print("Path:", path)
print("Cost:", cost)
