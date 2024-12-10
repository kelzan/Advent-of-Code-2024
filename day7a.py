def calculate(operands, operators):
    acc = operands[0]
    for x in range(len(operands)-1):
        operator = operators & (1 << x)
        if (operator):
            result = acc + operands[x+1]
            # print(f"{result} = {acc} + {operands[x+1]}")
        else:
            result = acc * operands[x+1]
            # print(f"{result} = {acc} * {operands[x+1]}")
        acc = result
    return acc


def read_and_process(file_path):
    tally = 0
    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by any amount of whitespace
            parts = line.split(':')
            target = int(parts[0])

            strlist = parts[1].split()
            intlist = [int(num) for num in strlist]

            # print(target, intlist)

            iterations = (1 << (len(intlist)-1))
            # print(f"iterations: {iterations}")
            for i in range(iterations):
                result = calculate(intlist, i)
                # print(f"iteration {i}, result: {result}, target {target}")
                if (result == target):
                    tally += target
                    break
    return tally

            


# Example usage
file_path = 'day7a_input.txt'  # Replace with your file path
sum = read_and_process(file_path)

print(f"Calibration result: {sum}")
