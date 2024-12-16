import numpy as np

# The input file contains:
# - A warehouse map where:
#   - `#` represents walls
#   - `O` represents boxes
#   - `@` represents the robot
# - A blank line separating the map from the robot's movements
# - The robot's movements represented by characters:
#   - `<` move left
#   - `>` move right
#   - `^` move up
#   - `v` move down

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Separate the map and the movements
    blank_line_index = lines.index('\n')
    map_lines = lines[:blank_line_index]
    movement_lines = lines[blank_line_index + 1:]
    
    # Parse the map into a 2D numpy array
    warehouse_map = np.array([list(line.strip()) for line in map_lines])
    
    # Parse the movements into a single string
    movements = ''.join(line.strip() for line in movement_lines)
    
    return warehouse_map, movements

def print_warehouse_map(warehouse_map):
    for row in warehouse_map:
        print(''.join(row))

def translate_warehouse_map(warehouse_map):
    translation = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.'
    }
    new_map = []
    for row in warehouse_map:
        new_row = ''.join(translation[tile] for tile in row)
        new_map.append(list(new_row))
    return np.array(new_map)

def move_robot(warehouse_map, move):
    direction = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    dx, dy = direction[move]
    robot_pos = np.argwhere(warehouse_map == '@')[0]
    x, y = robot_pos

    def can_move(x, y, dx, dy):
        next_x, next_y = x + dx, y + dy
        if warehouse_map[next_x, next_y] == '#' or warehouse_map[next_x, next_y + 1] == '#':
            return False
        if warehouse_map[next_x, next_y] == '[' and warehouse_map[next_x, next_y + 1] == ']':
            next_x += dx
            next_y += dy
            if warehouse_map[next_x, next_y] == '#' or warehouse_map[next_x, next_y + 1] == '#':
                return False
        return True

    if can_move(x, y, dx, dy):
        next_x, next_y = x + dx, y + dy
        if warehouse_map[next_x, next_y] == '[' and warehouse_map[next_x, next_y + 1] == ']':
            while warehouse_map[next_x, next_y] == '[' and warehouse_map[next_x, next_y + 1] == ']':
                next_x += dx
                next_y += dy
                if warehouse_map[next_x, next_y] == '#' or warehouse_map[next_x, next_y + 1] == '#':
                    break
            warehouse_map[next_x, next_y] = '['
            warehouse_map[next_x, next_y + 1] = ']'
        warehouse_map[x, y] = '.'
        warehouse_map[x, y + 1] = '.'
        warehouse_map[x + dx, y + dy] = '@'
        warehouse_map[x + dx, y + dy + 1] = '.'

def calculate_total_score(warehouse_map):
    total_score = 0
    for x in range(warehouse_map.shape[0]):
        for y in range(warehouse_map.shape[1]):
            if warehouse_map[x, y] == 'O':
                total_score += 100 * x + y
                print(f"Box at ({x}, {y}) score: {100 * y + x}")
    return total_score

# Example usage
warehouse_map, movements = parse_input('day15a_exam3.txt')
warehouse_map = translate_warehouse_map(warehouse_map)
print_warehouse_map(warehouse_map)
print(movements)

for move in movements:
    move_robot(warehouse_map, move)
    print(move)
    print_warehouse_map(warehouse_map)

total_score = calculate_total_score(warehouse_map)
print(f"Total score: {total_score}")
