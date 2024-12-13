"""Garden Groups
Calculate the area and perimeter of each type of plant. From that, calculate the total
cost of fencing."""

import numpy as np

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

def print_map(garden_map):
    """Prints the topo map to the console."""
    num_rows, num_cols = garden_map.shape

    for y in range(num_rows):
        print(*garden_map[y], sep='')

def parse_garden_map(garden_map):
    """Parses the garden map and populates the plot_areas dictionary with the areas of each plant type."""
    num_rows, num_cols = garden_map.shape
    for y in range(num_rows):
        for x in range(num_cols):
            plant_type = garden_map[y, x]
            if plant_type not in plot_areas:
                plot_areas[plant_type] = 0
            plot_areas[plant_type] += 1

def calculate_perimeters(garden_map):
    """Calculates the perimeter of each plant type and populates the plot_perimeters dictionary."""
    num_rows, num_cols = garden_map.shape
    for y in range(num_rows):
        for x in range(num_cols):
            plant_type = garden_map[y, x]
            if plant_type not in plot_perimeters:
                plot_perimeters[plant_type] = 0
            # Check each of the four sides
            if y == 0 or garden_map[y-1, x] != plant_type:  # Top side
                plot_perimeters[plant_type] += 1
            if y == num_rows-1 or garden_map[y+1, x] != plant_type:  # Bottom side
                plot_perimeters[plant_type] += 1
            if x == 0 or garden_map[y, x-1] != plant_type:  # Left side
                plot_perimeters[plant_type] += 1
            if x == num_cols-1 or garden_map[y, x+1] != plant_type:  # Right side
                plot_perimeters[plant_type] += 1

def get_region_coordinates(garden_map, start_coord):
    """Returns a list of all coordinates of the region given the garden_map and a starting coordinate."""
    num_rows, num_cols = garden_map.shape
    start_y, start_x = start_coord
    plant_type = garden_map[start_y, start_x]
    visited = set()
    region_coords = []

    def dfs(y, x):
        if (y, x) in visited or y < 0 or y >= num_rows or x < 0 or x >= num_cols or garden_map[y, x] != plant_type:
            return
        visited.add((y, x))
        region_coords.append((y, x))
        # Explore neighbors
        dfs(y-1, x)  # Up
        dfs(y+1, x)  # Down
        dfs(y, x-1)  # Left
        dfs(y, x+1)  # Right

    dfs(start_y, start_x)
    return region_coords

def calculate_total_fencing_cost():
    """Calculates the total price of fencing all regions on the map."""
    total_cost = 0
    for plant_type in plot_areas:
        area = plot_areas[plant_type]
        perimeter = plot_perimeters[plant_type]
        print(f"Plant type: {plant_type}, Area: {area}, Perimeter: {perimeter}")
        total_cost += area * perimeter
    return total_cost

plot_areas = {} # Dictionary to store the area of each plant type
plot_perimeters = {} # Dictionary to store the perimeter of each plant type

file_path = 'day12a_exam.txt'
garden_map = read_map(file_path)
parse_garden_map(garden_map)
calculate_perimeters(garden_map)
print_map(garden_map)

total_fencing_cost = calculate_total_fencing_cost()
print(f"Total cost of fencing: {total_fencing_cost}")

# Example usage of get_region_coordinates
start_coord = (0, 0)  # Example starting coordinate
region_coords = get_region_coordinates(garden_map, start_coord)
print(f"Region coordinates starting from {start_coord}: {region_coords}")