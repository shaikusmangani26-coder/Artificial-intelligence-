from collections import deque

def water_jug(jug1, jug2, target):
    queue = deque([(0, 0)])
    visited = set()
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Goal condition
        if x == target or y == target:
            path = []
            state = (x, y)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            path.reverse()

            print("Solution:")
            for state in path:
                print(state)
            return

        # Possible next states
        next_states = [
            (jug1, y),  # Fill jug 1
            (x, jug2),  # Fill jug 2
            (0, y),     # Empty jug 1
            (x, 0),     # Empty jug 2
        ]

        # Pour jug 1 -> jug 2
        pour = min(x, jug2 - y)
        next_states.append((x - pour, y + pour))

        # Pour jug 2 -> jug 1
        pour = min(y, jug1 - x)
        next_states.append((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                if state not in parent:
                    parent[state] = (x, y)
                queue.append(state)

    print("No solution exists.")


water_jug(4, 3, 2)
