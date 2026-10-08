from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# boat_position: 0 = left, 1 = right

def is_valid(m, c):
    # Number of people on the right side
    mr = 3 - m
    cr = 3 - c

    # Check left side
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    # Check right side
    if mr > 0 and mr < cr:
        return False

    return True


def get_next_states(state):
    m, c, boat = state

    # Possible boat movements
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]

    next_states = []

    for dm, dc in moves:
        if boat == 0:  # Boat moves left to right
            new_m = m - dm
            new_c = c - dc
            new_boat = 1
        else:           # Boat moves right to left
            new_m = m + dm
            new_c = c + dc
            new_boat = 0

        new_state = (new_m, new_c, new_boat)

        if is_valid(new_m, new_c):
            next_states.append(new_state)

    return next_states


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


# Find solution
solution = solve()

# Display solution
if solution:
    print("Solution found:\n")

    for i, state in enumerate(solution):
        m, c, boat = state

        side = "Left" if boat == 0 else "Right"

        print(
            f"Step {i}: "
            f"Missionaries = {m}, Cannibals = {c}, "
            f"Boat = {side}"
        )
else:
    print("No solution found.")
