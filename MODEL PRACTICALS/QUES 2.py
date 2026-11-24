import random
import math

N = 8

def conflicts(b):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(b[i]-b[j]) == abs(i-j):
                count += 1
    return count

def solve():
    b = list(range(N))
    random.shuffle(b)
    t = 100

    while t > 0.01:
        if conflicts(b) == 0:
            return b

        new = b[:]
        i, j = random.sample(range(N), 2)
        new[i], new[j] = new[j], new[i]

        delta = conflicts(new) - conflicts(b)

        if delta < 0 or random.random() < math.exp(-delta/t):
            b = new

        t *= 0.99

    return b if conflicts(b) == 0 else None

b = solve()

if b:
    print("Final Board:")
    for r in range(N):
        print(" ".join("Q" if b[c] == r else "." 
                       for c in range(N)))
else:
    print("Solution not found. Run again.")
