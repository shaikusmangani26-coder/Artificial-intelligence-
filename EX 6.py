
# Vacuum Cleaner Problem in AI

# Initial state of rooms
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Initial position of vacuum cleaner
position = 'A'

print("Initial State:", rooms)
print("Vacuum cleaner starts in Room", position)

# Clean both rooms
for room in ['A', 'B']:
    position = room
    print("\nVacuum cleaner moves to Room", position)

    if rooms[position] == 'Dirty':
        rooms[position] = 'Clean'
        print("Room", position, "is cleaned.")
    else:
        print("Room", position, "is already clean.")

# Display final state
print("\nFinal State:", rooms)
print("All rooms are clean.")
