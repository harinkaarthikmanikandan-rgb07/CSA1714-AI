from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(
        abs(i // 3 - (v - 1) // 3) +
        abs(i % 3 - (v - 1) % 3)
        for i, v in enumerate(state) if v != 0
    )

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)

                if new not in visited:
                    heappush(pq, (
                        g + 1 + heuristic(new),
                        g + 1, new, path + [state]
                    ))

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
result = solve(start)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution")
