import numpy as np
with open('input.txt') as f:
    text =  [list(line.strip('\n')) for line in f]

grid = np.array(text)

current_position = np.where(grid == '^')
direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
rotate_right_90 = {'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'}
facing = 'U'
i, j = current_position


while (i < len(grid) and j < len(grid[0])) and (i >= 0 and j >= 0):
    future_pos = (current_position[0] + direction_map[facing][0], current_position[1] + direction_map[facing][1])
    if future_pos[0] >= len(grid) or future_pos[1] >= len(grid[0]) or future_pos[0] < 0 or future_pos[1] < 0:
        break
    if grid[future_pos] == '#':
        new_face = rotate_right_90[facing]
        facing = new_face
    else:
        grid[(i,j)] = 'X'
        current_position = future_pos
    # print(grid)
    i, j = current_position
print(len(np.where(grid == 'X')[0])+1)