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
    print(f"size - {num_rows} rows, {num_cols} cols")
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
        if (room_map[nexty,nextx] == '#'):
            current_direction = current_direction.next()
        else:
            room_map[nexty,nextx] = 'X'
            cury, curx = nexty, nextx
        # i += 1
        # print(i)
        # if (i>30):
        #     searching = False


# Example usage
file_path = 'day6a_input.txt'
room_map = read_map(file_path)
make_moves(room_map)
# print(room_map)
print_map(room_map)

# Count 'X' in the array
count_x = np.count_nonzero(room_map == 'X')

print(f"Total Count: {count_x}")  # This will output the number of 'X's in your array