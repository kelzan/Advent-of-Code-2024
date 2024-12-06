
import re


def read_and_process(file_path):
    total = 0
    mpattern = r'mul\((\d+),(\d+)\)'
    dopattern = r'do\(\)'
    dontpattern = r'don\'t\(\)'


    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
        pos = 0
        active = True
        while (pos < len(content)):
            if active:
                match = re.match(mpattern, content[pos:])
                if match:
                    #num1, num2 = map(int, match)
                    num1 = int(match.group(1))
                    num2 = int(match.group(2))
                    print(f"Found mul {num1} * {num2}")
                    total += num1 * num2
            if (re.match(dopattern, content[pos:])):
                active = True
            if (re.match(dontpattern, content[pos:])):
                active = False
            pos += 1
    return total



numtotal = read_and_process("day3_input.txt")
print(f"Total: {numtotal}")