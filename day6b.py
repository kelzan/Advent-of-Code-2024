import numpy as np
from enum import Enum, auto

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def next(self):
        # List of directions in the order they should cycle
        directions = list(Direction)
        
        # Find the current index in the list of directions
        current_index = directions.index(self)
        
        # Move to the next direction, wrapping around if necessary
        next_index = (current_index + 1) % len(directions)
        
        return directions[next_index]

dir_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def read_map(file_path):
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # Strip newline characters and ensure all rows are of equal length
        grid = [list(line.strip()) for line in lines]
        
        # Convert the list of lists to a NumPy array
        np_grid = np.array(grid)
    
    return np_grid

def find_start(room_map):
    num_rows, num_cols = room_map.shape
    for y in range(num_rows):
        for x in range(num_cols):
            if (room_map[y,x] == '^'):
                return y, x
    return -1, -1

def print_map(room_map):
    num_rows, num_cols = room_map.shape
    cury, curx = find_start(room_map)

    for y in range(num_rows):
        for x in range(num_cols):
            print(room_map[y,x], end='')
        print()

def make_moves(room_map):
    num_rows, num_cols = room_map.shape
    current_direction = Direction.UP
    # print(f"size - {num_rows} rows, {num_cols} cols")
    cury, curx = find_start(room_map)
    room_map[cury, curx] = 'X'
    i = 0

    searching = True
    while searching:
        # print_map(room_map)
        movement = dir_offsets[current_direction.value]
        nextx = curx + movement[1]
        nexty = cury + movement[0]
        # print(f"current {cury},{curx} - Next {nexty},{nextx}")
        if ((nexty < 0) or (nextx < 0) or (nexty >= num_rows) or (nextx >= num_cols)):
            searching = False
            continue
        if ((room_map[nexty,nextx] == '#') or (room_map[nexty,nextx] == 'O')):
            current_direction = current_direction.next()
        else:
            if (room_map[nexty,nextx] == str(current_direction.value)):
                return True
            # room_map[nexty,nextx] = 'X'
            room_map[nexty,nextx] = str(current_direction.value)
            cury, curx = nexty, nextx



# Example usage
file_path = 'day6a_input.txt'
room_map = read_map(file_path)
# print_map(room_map)

num_rows, num_cols = room_map.shape
print(f"size - {num_rows} rows, {num_cols} cols")
solution_map = room_map.copy()

success = 0
for y in range(num_rows):
    for x in range(num_cols):
# for y in range(3):
#     for x in range(2):
        if ((room_map[y,x] != '#') and (room_map[y,x] != '^')):
            new_map = room_map.copy()
            new_map[y,x] = 'O'
            if (make_moves(new_map)):
                # print_map(new_map)
                # print("REPEAT!")
                success += 1
                solution_map[y,x] = 'O'
            # else:
            #     print_map(new_map)
            #     print("FAIL")

print_map(solution_map)
print(f"Total Success: {success}")

# make_moves(room_map)
# # print(room_map)

