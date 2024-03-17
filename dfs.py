visited = []
stack = []
graph={}
def dfs(search_value, visited, stack, graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            node = graph[i][j]
            if node not in visited:
                visited.append(node)
                stack.append(node)

                if search_value == node:
                   # print(f"Value {search_value} found at index ({i}, {j})")
                    return True
    return False
                # You may want to recursively call dfs on neighbors here

# Example usage
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

result=dfs(2, visited, stack, graph)

print(result)
