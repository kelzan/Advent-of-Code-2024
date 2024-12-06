import numpy as np

def read_word_search(file_path):
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # Strip newline characters and ensure all rows are of equal length
        grid = [list(line.strip()) for line in lines]
        
        # Convert the list of lists to a NumPy array
        np_grid = np.array(grid)
    
    return np_grid

def search_string(puzzle, curx, cury):
    if (puzzle[cury, curx] != "A"):
        return 0
    # Get the number of rows and columns
    num_rows, num_cols = puzzle.shape
    if ((cury < 1) or (curx < 1) or (cury > (num_rows - 2)) or (curx > (num_rows - 2))):
        return 0
    if ((((puzzle[cury-1,curx-1] == "S") and (puzzle[cury+1,curx+1] == "M")) or
        ((puzzle[cury-1,curx-1] == "M") and (puzzle[cury+1,curx+1] == "S"))) and
        (((puzzle[cury-1,curx+1] == "S") and (puzzle[cury+1,curx-1] == "M")) or
        ((puzzle[cury-1,curx+1] == "M") and (puzzle[cury+1,curx-1] == "S")))):
        print(f"Match at {curx},{cury}")
        return 1
    return 0
        

# Example usage
file_path = 'day4a_input.txt'
puzzle = read_word_search(file_path)

# Get the number of rows and columns
num_rows, num_cols = puzzle.shape

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

matches = 0
for y in range(num_rows):
    for x in range(num_cols):
        matches += search_string(puzzle, x, y)

# Example: Print the entire puzzle
print(puzzle)
print(f"Matches: {matches}")