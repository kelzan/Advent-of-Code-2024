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

def search_string(puzzle, text, curx, cury, dirx, diry):
    # Get the number of rows and columns
    num_rows, num_cols = puzzle.shape
    for char in text:
        if ((cury < 0) or (curx < 0) or (cury >= num_rows) or (curx >= num_cols)):
            return 0
        if (char != puzzle[cury, curx]):
            return 0
        cury += diry
        curx += dirx
    return 1
        

# Example usage
file_path = 'day4a_input.txt'
puzzle = read_word_search(file_path)

# # Now you can access characters by row and column
# row_index = 2
# column_index = 3
# char_at_position = puzzle[row_index, column_index]
# print(char_at_position)

# Get the number of rows and columns
num_rows, num_cols = puzzle.shape

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

matches = 0
for y in range(num_rows):
    for x in range(num_cols):
        # Search right
        matches += search_string(puzzle, "XMAS", x, y, 1, 0)
        # Search left
        matches += search_string(puzzle, "XMAS", x, y, -1, 0)
        # Search up
        matches += search_string(puzzle, "XMAS", x, y, 0, -1)
        # Search down
        matches += search_string(puzzle, "XMAS", x, y, 0, 1)
        # Search up-right
        matches += search_string(puzzle, "XMAS", x, y, 1, -1)
        # Search down-right
        matches += search_string(puzzle, "XMAS", x, y, 1, 1)
        # Search up-left
        matches += search_string(puzzle, "XMAS", x, y, -1, -1)
        # Search down-left
        matches += search_string(puzzle, "XMAS", x, y, -1, 1)

# Example: Print the entire puzzle
# print(puzzle)
print(f"Matches: {matches}")