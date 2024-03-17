import random

def search_with_closed_list(graph, initial_node, target_node):
    current_node = initial_node
    visited = {initial_node}  # Initialize a set to keep track of visited nodes
    path = [current_node]  # Initialize path with the initial node

    while current_node != target_node:
        if current_node == target_node:
            return True, path  # Success

        child_nodes = [node for node in graph.get(current_node, []) if node not in visited]
       
        if not child_nodes:
            return False, path  # Failure if there are no unvisited child nodes
        random.shuffle(child_nodes)
        next_node = random.choice(child_nodes)  # Choose a random unvisited child node
        current_node = next_node
        visited.add(current_node)  # Mark the chosen node as visited
        path.append(current_node)  # Add the chosen node to the path

    return True, path  # Success if the target node is reached
'''
# Given graph
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],                 
    4: [],
    5: [],
    6: [],
    7: [],
    8: []
}

# Initial and target nodes
initial_node = 0
target_node = 8

# Perform random search and get the result and path
result, path = search_with_closed_list(graph, initial_node, target_node)

if result:
    print(f"The path from {initial_node} to {target_node} is: {path}")  # Subtract 1 to get the number of edges
else:
    print("Target node not reachable from the initial node.")
'''