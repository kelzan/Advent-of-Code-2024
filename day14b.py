import numpy as np

MAP_X_SIZE = 101
MAP_Y_SIZE = 103
NUMBER_OF_STEPS = 100

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update_position(self, x_size, y_size):
        new_x = (self.position[0] + self.velocity[0]) % x_size
        new_y = (self.position[1] + self.velocity[1]) % y_size
        self.position = (new_x, new_y)

def parse_file(filepath):
    robots = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0][2:].split(',')))
            vel = tuple(map(int, parts[1][2:].split(',')))
            robots.append(Robot(pos, vel))
    return robots

def initialize_map(x_size, y_size):
    return np.full((y_size, x_size), '.')

def print_map(map_array):
    for row in map_array:
        print(''.join(row))

def update_map_with_robots(map_array, robots):
    map_array[:, :] = '.'  # Reinitialize all spots to '.'
    for robot in robots:
        x, y = robot.position
        if map_array[y, x] == '.':
            map_array[y, x] = '1'
        else:
            map_array[y, x] = str(int(map_array[y, x]) + 1)

def count_robots_in_quadrants(robots, x_size, y_size):
    mid_x = x_size // 2
    mid_y = y_size // 2
    q1 = q2 = q3 = q4 = 0

    for robot in robots:
        x, y = robot.position
        if x == mid_x or y == mid_y:
            continue  # Robots on the middle lines don't count
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x >= mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1

    return q1, q2, q3, q4

if __name__ == "__main__":
    filepath = 'day14a_input.txt'
    robots = parse_file(filepath)

    map_array = initialize_map(MAP_X_SIZE, MAP_Y_SIZE)
    update_map_with_robots(map_array, robots)
    print_map(map_array)
    print(f"Number of robots found: {len(robots)}")

    steps = 0
    while True:
        for robot in robots:
            robot.update_position(MAP_X_SIZE, MAP_Y_SIZE)
        steps += 1
        update_map_with_robots(map_array, robots)
        # Find the maximum number of robots in the same spot
        # Replace non-numeric values with 0
        map_array_int = np.array([[int(cell) if cell.isdigit() else 0 for cell in row] for row in map_array])
        # Find the maximum number of robots in the same spot
        max_robots = np.max(map_array_int.flatten())
        # max_robots = np.max(np.array(list(map_array.flatten())))
        if max_robots == 1:
            break
        
    print_map(map_array)
    print(f"After {steps} steps:")

