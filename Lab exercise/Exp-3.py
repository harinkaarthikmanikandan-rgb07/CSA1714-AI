from collections import deque

def water_jug():
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        if a == 2 or b == 2:
            return path

        states = [
            (4, b), (a, 3), (0, b), (a, 0),
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            (a + min(b, 4 - a), b - min(b, 4 - a))
        ]

        for state in states:
            if state not in visited:
                queue.append((state, path))

    return None

result = water_jug()

for state in result:
    print(state)
