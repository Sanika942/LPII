def dijkstra(graph, start):
    # Initialize distances and visited set
    distances = {chr(i + ord('A')): float('inf') for i in range(len(graph))}
    visited = set()

    # Set distance of start vertex to 0
    distances[start] = 0

    while len(visited) < len(graph):
        # Find the vertex with the smallest tentative distance
        min_vertex = None
        min_distance = float('inf')
        for vertex, distance in distances.items():
            if vertex not in visited and distance < min_distance:
                min_vertex = vertex
                min_distance = distance

        # Mark the selected vertex as visited
        visited.add(min_vertex)

        # Update distances to neighbors of the selected vertex
        for neighbor, weight in enumerate(graph[ord(min_vertex) - ord('A')]):
            if weight > 0:
                distances[chr(neighbor + ord('A'))] = min(distances[chr(neighbor + ord('A'))], distances[min_vertex] + weight)

    return distances

# Example usage:
adjacency_matrix = [
    [0, 4, 5, 0, 0, 0],
    [4, 0, 11, 9, 7, 0],
    [5, 11, 0, 0, 3, 0],
    [0, 9, 0, 0, 13, 2],
    [0, 7, 3, 13, 0, 6],
    [0, 0, 0, 2, 6, 0]
]
start_vertex = 'A'
shortest_distances = dijkstra(adjacency_matrix, start_vertex)
print("Shortest distances from vertex", start_vertex, ":", shortest_distances)
