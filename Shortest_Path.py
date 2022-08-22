def shortest_path(graph, source, target):
    # Mark everything as unvisited
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    
    # Set all distances to inf
    distance = [float('inf')] * len(graph.data)
    queue = []
    
    distance[source] = 0
    queue.append(source)
    idx = 0
    
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1
         
        # Update distances of all neighbors
        update_distances(graph, current, distance, parent)
        
        # Find first unvisited node with smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        
    
    return distance[target], parent
        
        
def update_distances(graph, current, distance, parent=None):
    """Update the distances of current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
        if parent:
            parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next unvisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
    
