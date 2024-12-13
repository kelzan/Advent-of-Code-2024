"""First read the input file and create a 2 dimensional topo map consisting of integers between 0 and 9,
which represent the height of the terrain. A trailhead starts at a location with a height of 0, and a valid
trail consists of adjacent locations with a height difference of 1. A valid trail is one which starts at 0 and
goes to 9. The score of a trailhead is the sum of how many valid trails can be started from that location.
We need to find the sum of the scores of all trailheads."""
import numpy as np
from collections import deque

def read_map(file_path):
    """Reads the topo map from the specified file and returns it as a NumPy array."""
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # Strip newline characters and ensure all rows are of equal length
        grid = [list(line.strip()) for line in lines]
        
        # Convert the list of lists to a NumPy array
        np_grid = np.array(grid)
    
    return np_grid

def convert_char_to_int(char):
    """Converts a character to an integer after checking that it's a digit.
    if it's not a digit, it returns -1"""
    if char.isdigit():
        return int(char)
    else:
        return -10

def score_trailhead(topo_map, y, x):
    """Scores a trailhead at the specified location."""
    num_rows, num_cols = topo_map.shape
    score = 0
    # score = np.zeros((num_rows, num_cols), dtype=int)
    
    # Check if the location is a trailhead
    if topo_map[y, x] == '0':
        # Initialize a queue with the trailhead location
        candidates = deque([(y, x)])

        while candidates:
            # print(candidates)
            current_y, current_x = candidates.popleft()

            # Check if the current location is a valid trailhead ending
            if topo_map[current_y, current_x] == '9':
                score += 1
            else:
                # Add adjacent locations to the queue
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_y, new_x = current_y + dy, current_x + dx
                    if 0 <= new_y < num_rows and 0 <= new_x < num_cols and \
                    convert_char_to_int(topo_map[new_y, new_x]) == convert_char_to_int(topo_map[current_y, current_x]) + 1:
                        candidates.append((new_y, new_x))

    return score

def score_all_trailheads(topo_map):
    """Scores all trailheads in the topo map."""
    num_rows, num_cols = topo_map.shape
    scores = np.zeros((num_rows, num_cols), dtype=int)

    for y in range(num_rows):
        for x in range(num_cols):
            scores[y, x] = score_trailhead(topo_map, y, x)
    return scores

def print_map(topo_map):
    """Prints the topo map to the console."""
    num_rows, num_cols = topo_map.shape

    for y in range(num_rows):
        print(*topo_map[y], sep='')

file_path = 'day10a_input.txt'
topo_map = read_map(file_path)
print_map(topo_map)
scores = score_all_trailheads(topo_map)
print_map(scores)
print(f"Total score: {scores.sum()}")

