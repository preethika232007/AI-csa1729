import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    frontier = [(0, start)]
    came_from = {start: None}
    cost = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for dx, dy in [(0, 1), (0, -1),
                       (1, 0), (-1, 0)]:

            neighbor = (current[0] + dx,
                        current[1] + dy)

            if 0 <= neighbor[0] < 5 and 0 <= neighbor[1] < 5:
                new_cost = cost[current] + 1

                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)

                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path, cost[goal]


start = (0, 0)
goal = (4, 4)

path, cost = astar(start, goal)

print("Shortest path:", path)
print("Cost:", cost)
