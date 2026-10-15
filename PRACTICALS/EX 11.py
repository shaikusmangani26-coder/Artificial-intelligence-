
# Map Coloring using CSP (Backtracking)

# Define the map and neighboring regions
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store color assignments
assignment = {}


def is_valid(region, color):
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def map_coloring(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if map_coloring(regions[1:]):
                return True

            # Backtrack
            del assignment[region]

    return False


# Solve the CSP
regions = list(graph.keys())

if map_coloring(regions):
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists.")
