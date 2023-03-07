import heapq

def shortest_path(matrix, start, end):
    # Initialize variables
    n = len(matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    queue = [(0, start)]
    path = {}
    heapq.heapify(queue)

    # Main loop
    while queue:
        # Get the next node to visit
        (dist, node) = heapq.heappop(queue)

        # Stop if we reach the end node
        if node == end:
            break

        # Visit the node if we haven't already
        if not visited[node]:
            visited[node] = True

            # Update distances for neighboring nodes
            for i in range(n):
                if matrix[node][i] != 0:
                    new_dist = dist + matrix[node][i]
                    if new_dist < distances[i]:
                        distances[i] = new_dist
                        path[i] = node
                        heapq.heappush(queue, (new_dist, i))

    # Build the path from start to end
    shortest_path = [end]
    path_tuples = []
    #shortest_path1 = [(start,end)]
    while end != start:
        shortest_path.append(path[end])
        path_tuples.append((path[end], end))
        #start = path[end]
        #shortest_path1.append(tuple(path[start],path[end]))
        #start = path[start]
        end = path[end]
    shortest_path.reverse()
    #path_tuples.append(start)
    path_tuples.reverse()
    #shortest_path1.reverse()

    print(shortest_path)
    print(path_tuples)
    #print(shortest_path1)

"""
# Define the graph as a matrix
graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 2, 5, 0],
    [4, 2, 0, 1, 3],
    [0, 5, 1, 0, 2],
    [0, 0, 3, 2, 0]
]

# Define the start and end nodes
start = 0
end = 4

#call function
shortest_path(graph, start, end)
"""
