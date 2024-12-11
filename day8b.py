import numpy as np
from enum import Enum, auto
from itertools import combinations

def read_map(file_path):
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # Strip newline characters and ensure all rows are of equal length
        grid = [list(line.strip()) for line in lines]
        
        # Convert the list of lists to a NumPy array
        np_grid = np.array(grid)
    
    return np_grid

def scan_antennas(room_map):
    antennas = {}
    num_rows, num_cols = room_map.shape

    for y in range(num_rows):
        for x in range(num_cols):
            locchar = str(room_map[y,x])
            if (locchar != "."):
                if (locchar in antennas):
                    antennas[locchar].append((y,x))
                else:
                    antennas[locchar] = [(y,x)]
    return antennas

def points_on_line(grid_max_x, grid_max_y, point1, point2):
    # Extract coordinates
    x1, y1 = point1
    x2, y2 = point2
    
    # Calculate the difference in coordinates
    dx = x2 - x1
    dy = y2 - y1
    
    # Find the greatest common divisor to normalize direction
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    step = gcd(abs(dx), abs(dy))
    
    if step == 0:  # Points are the same, return both or just one
        return [point1] if point1 == point2 else [point1, point2]
    
    # Normalize dx and dy
    dx //= step
    dy //= step
    
    # Generate points
    points = []
    for i in range(int(step) + 1):
        x = x1 + i * dx
        y = y1 + i * dy
        if 0 <= x <= grid_max_x and 0 <= y <= grid_max_y:
            points.append((x, y))
    
    # Extend the line in both directions
    # Forward direction
    i = 1
    while True:
        x = x2 + i * dx
        y = y2 + i * dy
        if 0 <= x <= grid_max_x and 0 <= y <= grid_max_y:
            points.append((x, y))
        else:
            break
        i += 1
    
    # Backward direction
    i = 1
    while True:
        x = x1 - i * dx
        y = y1 - i * dy
        if 0 <= x <= grid_max_x and 0 <= y <= grid_max_y:
            points.insert(0, (x, y))  # Insert at the beginning for backward extension
        else:
            break
        i += 1
    
    return points

def distance(point1, point2):
    return (abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]))

def print_map(room_map):
    num_rows, num_cols = room_map.shape

    for y in range(num_rows):
        for x in range(num_cols):
            print(room_map[y,x], end='')
        print()


# antenna_locs = {}

file_path = 'day8a_input.txt'
room_map = read_map(file_path)
antenna_locs = scan_antennas(room_map)
# make_moves(room_map)
# print(room_map)
print_map(room_map)
print(antenna_locs)
print(antenna_locs.keys())
num_rows, num_cols = room_map.shape

for key in antenna_locs:
    print(f"KEY: {key}")
    ant_pairs = list(combinations(antenna_locs[key], 2))
    print(ant_pairs)

    for ant_pair in ant_pairs:
        line = points_on_line(num_rows-1, num_cols-1, ant_pair[0], ant_pair[1])
        print("line: ",line)
        for point in line:
            # distance1 = distance(ant_pair[0],point)
            # distance2 = distance(ant_pair[1], point)
            # print(f"distance from {point} to {ant_pair[0]} is {distance1}, to {ant_pair[1]} is {distance2}")
            # if ((distance1 == (2*distance2)) or (distance2 == (2*distance1))):
            room_map[point] = '#'

print_map(room_map)

count_nodes = np.count_nonzero(room_map == '#')
print(f"Antinodes: {count_nodes}")
