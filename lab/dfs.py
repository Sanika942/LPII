graph = {
    '5': ['3', '7'],
    '3': ['5', '2', '4'],
    '7': ['5', '8'],
    '2': ['3'],
    '4': ['3', '8'],
    '8': ['7', '4']
}

visited = set()  # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')


