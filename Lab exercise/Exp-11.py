# Map Coloring using Constraint Satisfaction Problem (CSP)

def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve_map_coloring(graph, colors, assignment={}):
    # If all regions are colored
    if len(assignment) == len(graph):
        return assignment

    # Select an unassigned region
    unassigned = [region for region in graph if region not in assignment]
    region = unassigned[0]

    # Try each color
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color

            result = solve_map_coloring(graph, colors, assignment)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None


graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

colors = ["Red", "Green", "Blue"]

solution = solve_map_coloring(graph, colors)

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution exists.")
