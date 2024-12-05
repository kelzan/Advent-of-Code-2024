
def is_safe(report):
    firstone = True
    direction = True
    for x in range(len(report)-1):
        if (report[x+1] > report[x]):
            ascending = True
        elif (report[x+1] < report[x]):
            ascending = False
        else:
            print("equal")
            return False
        diff = abs(report[x] - report[x+1])
        if ((diff < 1) or (diff > 3)):
            print("gap")
            return False
        if firstone:
            direction = ascending
            firstone = False
        elif (direction != ascending):
            print("direction")
            return False
    print("safe")
    return True



def read_and_process(file_path):
    # Initialize empty lists to store the numbers
    column1 = []
    column2 = []
    num_safe = 0

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by any amount of whitespace
            parts = line.split()
            print (parts)
            int_array = [int(x) for x in parts]
            if (is_safe(int_array)):
                num_safe += 1

    return num_safe


safe_reps = read_and_process("day2a_input.txt")
print(f"{safe_reps} safe reports")