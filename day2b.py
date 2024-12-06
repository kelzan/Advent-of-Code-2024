
def is_safe(full_report):
    for y in range(len(full_report)+1):
        report = full_report.copy()
        if (y>0):
            del report[y-1]
        print(f"Pass {y}", report, full_report)
        firstone = True
        direction = True
        passes = True
        for x in range(len(report)-1):
            if (report[x+1] > report[x]):
                ascending = True
            elif (report[x+1] < report[x]):
                ascending = False
            else:
                print("equal")
                passes = False
                break
                #return False
            diff = abs(report[x] - report[x+1])
            if ((diff < 1) or (diff > 3)):
                print("gap")
                passes = False
                break
                #return False
            if firstone:
                direction = ascending
                firstone = False
            elif (direction != ascending):
                print("direction")
                passes = False
                break
                #return False
        if (passes):
            print(f"Pass {y} is safe")
            return True
    return False



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
            #print (parts)
            int_array = [int(x) for x in parts]
            if (is_safe(int_array)):
                num_safe += 1

    return num_safe


safe_reps = read_and_process("day2a_input.txt")
print(f"{safe_reps} safe reports")