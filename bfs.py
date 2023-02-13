import pygame as pg
from collections import deque
from random import random

# Fungsi untuk mendapatkan rect dari grid
def get_grid_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

# Fungsi untuk mendapatkan node yang bersebelahan
def get_adjacent_nodes(x, y):
    within_bounds = lambda x, y: 0 <= x < cols and 0 <= y < rows
    walkable = lambda x, y: not grid[y][x]
    move_options = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]]
    return [(x + dx, y + dy) for dx, dy in move_options if within_bounds(x + dx, y + dy) and walkable(x + dx, y + dy)]

# Fungsi untuk mendapatkan node yang diklik
def get_clicked_node():
    mouse_pos = pg.mouse.get_pos()
    grid_x, grid_y = mouse_pos[0] // TILE, mouse_pos[1] // TILE
    pg.draw.rect(screen, pg.Color('pink'), get_grid_rect(grid_x, grid_y))
    mouse_clicks = pg.mouse.get_pressed()
    return (grid_x, grid_y) if mouse_clicks[0] else False

# Fungsi BFS
def breadth_first_search(start, goal, graph):
    q = deque([start])
    visited = {start: None}

    while q:
        curr = q.popleft()
        if curr == goal:
            break

        for adj in graph[curr]:
            if adj not in visited:
                q.append(adj)
                visited[adj] = curr
    return q, visited

if __name__ == '__main__':
    cols, rows = 25, 20
    TILE = 30

    # Inisialisasi pygame
    pg.init()
    screen = pg.display.set_mode([cols * TILE, rows * TILE])
    clock = pg.time.Clock()

    grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
    graph = {}
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if not col:
                graph[(x, y)] = graph.get((x, y), []) + get_adjacent_nodes(x, y)

    start, goal = (0, 0), (0, 0)
    bfs_queue, visited = deque([start]), {start: None}

    while True:
        screen.fill(pg.Color('darkslategray'))

        [[pg.draw.rect(screen, pg.Color('darkorange'), get_grid_rect(x, y), border_radius=TILE // 5)
          for x, col in enumerate(row) if col] for y, row in enumerate(grid)]

        [pg.draw.rect(screen, pg.Color("forestgreen"), get_grid_rect(x, y)) for x, y in visited]
        [pg.draw.rect(screen, pg.Color("lightgreen"), get_grid_rect(x, y)) for x, y in bfs_queue]


        # Melakukan BFS dan mendapatkan path dari mouse click
        mouse_pos = get_clicked_node()
        if mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
            bfs_queue, visited = breadth_first_search(start, mouse_pos, graph)
            goal = mouse_pos

        # Gambar path
        path_head, path_segment = goal, goal
        while path_segment and path_segment in visited:
            pg.draw.rect(screen, pg.Color("white"), get_grid_rect(*path_segment), TILE, border_radius=TILE // 3)
            path_segment = visited[path_segment]
        pg.draw.rect(screen, pg.Color("blue"), get_grid_rect(*start), border_radius=TILE // 3)
        pg.draw.rect(screen, pg.Color("magenta"), get_grid_rect(*path_head), border_radius=TILE // 3)

        # Periksa event apakah terdapat quit
        [exit() for event in pg.event.get() if event.type == pg.QUIT]
        pg.display.flip()
        clock.tick(30)

