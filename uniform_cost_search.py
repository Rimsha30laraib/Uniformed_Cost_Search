stack=[]
graph={}
def uniform_cost_search(graph, start_value, end_value, stack):
    min_value = float('inf')  # Initialize with positive infinity
    for neighbor, distance in graph[start_value].items():
        stack.append((neighbor, distance))

    while stack:
        current_node, current_distance = stack.pop(0)

        if current_node == end_value:
            return current_distance

        for neighbor, distance in graph[current_node].items():
            stack.append((neighbor, current_distance + distance))

    return float('inf')  # Return infinity if no path is found
'''
# Example usage
graph = {
    0: {1: 2, 2: 6},
    1: {0: 2, 3: 5},
    2: {0: 6, 3: 8},
    3: {1: 5, 2: 8, 4: 10},
    4: {3: 10, 6: 2},
    5: {3: 15, 6: 6},
    6: {4: 2, 5: 6}
}

start_value = 0
end_value = 6
stack = []
result = uniform_cost_search(graph, start_value, end_value, stack)
print(f"The minimum distance from {start_value} to {end_value} is: {result}")
'''