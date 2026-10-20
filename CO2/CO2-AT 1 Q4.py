
# Minimax Algorithm
# X = MAX player, O = MIN player

# Final scores from left to right
scores = [4, 7, 8, 2, 3, 5, 6, 9]

# Each pair represents X's final choices
x_values = []

for i in range(0, len(scores), 2):
    value = max(scores[i], scores[i + 1])
    x_values.append(value)
    print(
        f"X final choices: {scores[i]}, {scores[i+1]}"
        f" -> MAX = {value}"
    )

# O chooses the minimum reply value
o_values = []

for i in range(0, len(x_values), 2):
    value = min(x_values[i], x_values[i + 1])
    o_values.append(value)
    print(
        f"O reply values: {x_values[i]}, {x_values[i+1]}"
        f" -> MIN = {value}"
    )

# X chooses the best first move
best_score = max(o_values)
best_move = o_values.index(best_score) + 1

print("\nRoot value:", best_score)
print("Best first move: X", best_move)
print("Guaranteed score:", best_score)

# Follow optimal play
if best_move == 1:
    print("Optimal sequence: X1 -> O1 -> X chooses score 7")
else:
    print("Optimal sequence: X2 -> O1 -> X chooses score 5")
