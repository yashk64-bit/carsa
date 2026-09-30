import heapq

def a_star(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, 0, start))

    came_from = {}
    g_score = {start: 0}

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    directions = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)
    ]

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
           
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1]

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)

            r, c = neighbor

            if not (0 <= r < rows and 0 <= c < cols):
                continue

            if grid[r][c] == 1:  
                continue

            new_g = g_score[current] + 1

            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + heuristic(neighbor, goal)

                came_from[neighbor] = current

                heapq.heappush(
                    open_set,
                    (f_score, new_g, neighbor)
                )

    return None



grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)

print("Shortest path:", path)
