from collections import deque

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Possible movements of the blank space
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def solve_8_puzzle(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Check whether goal is reached
        if state == GOAL:
            return path + [state]

        zero = state.index(0)

        # Generate next states
        for new_pos in MOVES[zero]:
            new_state = list(state)

            # Swap blank with the neighboring tile
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


# Initial state
start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)

solution = solve_8_puzzle(start)

# Display solution
if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("\nStep", step)
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
else:
    print("No solution exists.")
