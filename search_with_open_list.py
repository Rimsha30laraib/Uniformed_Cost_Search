import random

def search_with_open_list(graph, initial_node, target_node):
    path = [initial_node]  # Initialize path with the initial node
    visited = set()  # Keep track of visited nodes

    while path:
        current_node = path[-1]  # Get the current node
        visited.add(current_node)

        if current_node == target_node:
            return True, path  # Success if the target node is found

        child_nodes = graph.get(current_node, [])
        unvisited_child_nodes = [node for node in child_nodes if node not in visited]

        if unvisited_child_nodes:  # If there are unvisited child nodes, choose one randomly
            next_node = random.choice(unvisited_child_nodes)
            path.append(next_node)
        else:  # If all child nodes have been visited, backtrack
            path.pop()

    return False, []  # If the loop terminates without finding the target node, return False
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
result, path = search_with_open_list(graph, initial_node, target_node)

# Print the result and path
if result:
    print(f"The path from {initial_node} to {target_node} is: {path}")
else:
    print(f"The target node {target_node} is not reachable from the initial node {initial_node}.")
'''