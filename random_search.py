import random

def random_search(graph, initial_node, target_node):
    visited = set()  # Initialize a set to keep track of visited nodes
    current_node = initial_node
    path = [current_node]
    while current_node != target_node:
        if current_node == target_node:
            return True  # Success if the target node is found

        visited.add(current_node)  # Add the current node to the visited set

        child_nodes = graph.get(current_node, []) 
        #print(child_nodes)
        unvisited_child_nodes = [node for node in child_nodes if node not in visited]

        if unvisited_child_nodes:
            next_node = random.choice(unvisited_child_nodes)  # Choose a random unvisited child node
            current_node = next_node
            path.append(current_node)
        elif visited:  # If all child nodes are visited, backtrack if possible
            current_node = visited.pop()  # Backtrack by selecting the last visited node
        else:
            return False  # Failure if there are no unvisited child nodes and the visited set is empty
        
    return True , path  # Success if the target node is reached
# Given graph
'''graph = {
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

# Perform random search and get the result
result, path = random_search(graph, initial_node, target_node)

if result:
    print(f"The path from {initial_node} to {target_node} is: {path}")  # Subtract 1 to get the number of edges
else:
    print("Target node not reachable from the initial node.")
'''