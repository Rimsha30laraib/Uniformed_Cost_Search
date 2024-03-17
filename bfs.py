from collections import deque
graph={}
def bfs(search_value, graph):
    visited = []
    queue =[]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            node = graph[i][j]
            if node not in visited:
                visited.append(node)
                queue.append(node)

                if search_value == node:
                    return True

    # Continue BFS for neighbors using the queue
    while queue:
        current_node = queue.popleft()

        # Process neighbors of current_node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

                if search_value == neighbor:
                    return True
'''
# Example usage
graph = {
    0: 1 2
    1: 3 4
    2: 5 6
    3: 7 8
    4
    5
    6
    7
    8
}

result=bfs(5, graph)
print(result)'''