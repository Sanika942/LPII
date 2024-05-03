graph = {
    '5': ['3', '7'],
    '3': ['5', '2', '4'],
    '7': ['5', '8'],
    '2': ['3'],
    '4': ['3', '8'],
    '8': ['7', '4']
}

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    node = queue.pop(0)
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
    bfs_recursive(graph, queue, visited)

# Driver Code
print("Following is the Breadth-First Search (Recursive)")
bfs_recursive(graph, ['5'])

