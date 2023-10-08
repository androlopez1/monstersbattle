from collections import deque


def find_less_cost_path(board: [[int]]) -> int:

    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Creamos una matriz para almacenar el costo mínimo hasta cada celda
    min_cost = [[float("inf")] * cols for _ in range(rows)]
    min_cost[0][0] = grid[0][0]

    # Creamos una cola para realizar BFS
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = min_cost[x][y] + grid[nx][ny]

                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    queue.append((nx, ny))

    return min_cost[rows - 1][cols - 1]


# Ejemplo de uso
grid = [[42, 51, 22, 10, 0], [2, 50, 7, 6, 15], [4, 36, 8, 30, 20], [0, 40, 10, 100, 1]]

result = find_less_cost_path(grid)
print("El menor costo de camino es:", result)
