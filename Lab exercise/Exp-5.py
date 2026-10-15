from collections import deque

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                nm, nc, nb = m - dm, c - dc, 1
            else:
                nm, nc, nb = m + dm, c + dc, 0

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            if ((nm > 0 and nm < nc) or
                (3 - nm > 0 and 3 - nm < 3 - nc)):
                continue

            new_state = (nm, nc, nb)

            if new_state not in visited:
                queue.append((new_state, path + [state]))

    return None

result = solve()

for state in result:
    print(state)
