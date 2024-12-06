
import re


def read_and_process(file_path):
    total = 0

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            pattern = r'mul\((\d+),(\d+)\)'
            matches = re.findall(pattern, line)
            for match in matches:
                num1, num2 = map(int, match)
                print(f"Found mul {num1} * {num2}")
                total += num1 * num2
    return total


numtotal = read_and_process("day3_input.txt")
print(f"Total: {numtotal}")