
# Alpha-Beta Pruning for a game engine

scores = {
    "M1": [6, 9, 7],
    "M2": [4, 8, 10],
    "M3": [7, 5, 12]
}

alpha = float("-inf")
beta = float("inf")
best_move = None
best_value = float("-inf")
scored = 0

for move, replies in scores.items():
    print("\nEvaluating", move)
    min_value = float("inf")

    for i, score in enumerate(replies):
        # Evaluate the current position
        scored += 1
        min_value = min(min_value, score)

        print("  Reply", i + 1, "score =", score)
        print("  MIN value =", min_value)
        print("  MAX alpha =", alpha)

        # Alpha-beta pruning at MIN node
        if min_value <= alpha:
            skipped = replies[i + 1:]
            if skipped:
                print("  PRUNED replies:", skipped)
            break

    # Update MAX's best choice
    if min_value > best_value:
        best_value = min_value
        best_move = move

    alpha = max(alpha, best_value)
    print("  Value of", move, "is at most", min_value)
    print("  Best move so far:", best_move)
    print("  Best MAX value:", alpha)

print("\nFinal best move:", best_move)
print("Guaranteed value:", best_value)
print("Positions actually scored:", scored)
print("Positions skipped:", 9 - scored)

# Verify by examining all nine scores
full_values = {
    move: min(values)
    for move, values in scores.items()
}
print("\nFull Minimax values:", full_values)
print("Full Minimax best move:", max(full_values, key=full_values.get))
