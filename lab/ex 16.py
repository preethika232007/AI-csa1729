from collections import deque

def bfs(adj_list, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}

start_node = 0
end_node = 4

shortest_path = bfs(graph, start_node, end_node)

if shortest_path is not None:
    print("The shortest path between",
          start_node, "and", end_node,
          "is", shortest_path)
else:
    print("There is no path")