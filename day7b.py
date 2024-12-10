from enum import Enum, auto

class Value(Enum):
    SUM = auto()
    MUL = auto()
    CONCAT = auto()

class ValueIterator:
    def __init__(self, num_values):
        self.num_values = num_values
        self.values = [Value.SUM] * num_values

    def increment(self):
        """
        Increments the first value in the list, carrying over if necessary.
        
        :return: bool indicating if increment was successful (False if saturated)
        """
        for i in range(self.num_values):
            if self.values[i] == Value.SUM:
                self.values[i] = Value.MUL
                return True
            elif self.values[i] == Value.MUL:
                self.values[i] = Value.CONCAT
                return True
            else:  # Value.CONCAT
                self.values[i] = Value.SUM
                if i == self.num_values - 1:  # Last value, can't carry over
                    return False
                # Continue to next position for carry over
        return False


def calculate(operands, operators):
    acc = operands[0]
    for x in range(len(operands)-1):
        # operator = operators & (1 << x)
        if (operators[x] == Value.SUM):
            result = acc + operands[x+1]
            # print(f"{result} = {acc} + {operands[x+1]}")
        elif (operators[x] == Value.MUL):
            result = acc * operands[x+1]
            # print(f"{result} = {acc} * {operands[x+1]}")
        elif (operators[x] == Value.CONCAT):
            result = int(str(acc) + str(operands[x+1]))
            # print(f"{result} = {acc} || {operands[x+1]}")
        else:
            print("What?",operators[x])
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
            vi = ValueIterator(len(intlist)-1)

            # iterations = (1 << (len(intlist)-1))
            # print(f"iterations: {iterations}")
            while True:
                result = calculate(intlist, vi.values)
                # print(f"iteration {vi.values}, result: {result}, target {target}")
                if (result == target):
                    tally += target
                    break
                if (not vi.increment()):
                    break
            print(f"Tally: {tally}")
    return tally

# Example usage
file_path = 'day7a_input.txt'  # Replace with your file path
sum = read_and_process(file_path)

print(f"Calibration result: {sum}")
