def f(x):
    return -(x - 3)**2 + 9

def hill_climbing(start):
    current = start

    while True:
        print("State:", current, "Value:", f(current))

        neighbors = [current - 1, current + 1]
        best = max(neighbors, key=f)

        if f(best) <= f(current):
            break

        current = best

    print("Maximum Value:", f(current))
    print("Best State:", current)

hill_climbing(0)
