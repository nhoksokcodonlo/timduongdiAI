my_map = [[0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
          [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]]


def number_islands_bfs(graph=my_map):
    queue = []

    if not graph:
        return 0

    row_total = len(graph)
    col_total = len(graph[0])

    count = 0

    for i in range(row_total):
        for j in range(col_total):
            if graph[i][j] != 1:
                continue

            count += 1
            queue.append((i, j))
            graph[i][j] = 2

            while queue:
                x, y = queue.pop()

                if x and graph[x-1][y] == 1:
                    queue.append((x-1, y))
                    graph[x-1][y] = 2

                if y and graph[x][y-1] == 1:
                    queue.append((x, y-1))
                    graph[x][y-1] = 2

                if x + 1 < row_total and graph[x+1][y] == 1:
                    queue.append((x+1, y))
                    graph[x+1][y] = 2

                if y+1 < col_total and graph[x][y+1] == 1:
                    queue.append((x, y+1))
                    graph[x][y+1] = 2

    return count


def number_islands_ucs(graph=my_map):
    return 0
print(f"Number of islands is {number_islands_bfs()}")