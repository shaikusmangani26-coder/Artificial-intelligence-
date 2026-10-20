
# Workshop Scheduling using CSP
# MRV + Degree Heuristic + Backtracking

workshops = ["W1", "W2", "W3", "W4", "W5"]

slots = ["Morning", "Afternoon", "Evening"]

domains = {
    "W1": slots.copy(),
    "W2": slots.copy(),
    "W3": ["Afternoon", "Evening"],
    "W4": ["Morning", "Afternoon"],
    "W5": slots.copy()
}

conflicts = [
    ("W1", "W2"),
    ("W1", "W3"),
    ("W2", "W3"),
    ("W2", "W4"),
    ("W3", "W5"),
    ("W4", "W5")
]

neighbors = {w: set() for w in workshops}

for a, b in conflicts:
    neighbors[a].add(b)
    neighbors[b].add(a)

assignment = {}


def is_consistent(workshop, slot):
    for other in neighbors[workshop]:
        if assignment.get(other) == slot:
            return False
    return True


def choose_workshop():
    unassigned = [
        w for w in workshops if w not in assignment
    ]

    # MRV: fewest legal slots remaining
    # Tie-break: highest number of unassigned conflicts
    return min(
        unassigned,
        key=lambda w: (
            sum(
                is_consistent(w, s)
                for s in domains[w]
            ),
            -sum(
                n not in assignment
                for n in neighbors[w]
            ),
            int(w[1:])
        )
    )


def backtrack():
    if len(assignment) == len(workshops):
        return True

    workshop = choose_workshop()

    # Try slots in the required order
    for slot in slots:
        if slot not in domains[workshop]:
            continue

        if is_consistent(workshop, slot):
            assignment[workshop] = slot

            print("\nAssigned:", workshop, "=", slot)

            # Forward checking: remove impossible slots
            saved_domains = {
                w: d.copy() for w, d in domains.items()
            }

            failure = False

            for other in neighbors[workshop]:
                if other not in assignment:
                    domains[other] = [
                        s for s in domains[other]
                        if s != slot
                    ]

                    print(
                        other, "remaining slots:",
                        domains[other]
                    )

                    if not domains[other]:
                        failure = True

            if not failure and backtrack():
                return True

            # Backtrack and restore domains
            domains.update(saved_domains)
            del assignment[workshop]
            print("Backtracking from", workshop, slot)

    return False


if backtrack():
    print("\nFinal Workshop Timetable")
    for w in workshops:
        print(w, ":", assignment[w])
else:
    print("No valid timetable exists.")
