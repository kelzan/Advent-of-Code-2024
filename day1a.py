print("Hello World!")

def read_and_sort_numbers(file_path):
    # Initialize empty lists to store the numbers
    column1 = []
    column2 = []

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by any amount of whitespace
            parts = line.split()
            # Convert string parts to float and append to lists
            if len(parts) >= 2:  # Ensure we have at least two columns
                column1.append(int(parts[0]))
                column2.append(int(parts[1]))

    # Sort both lists
    column1.sort()
    column2.sort()

    return column1, column2

# Example usage
file_path = 'day1a_input.txt'  # Replace with your file path
sorted_col1, sorted_col2 = read_and_sort_numbers(file_path)

print("Sorted Column 1:", sorted_col1)
print("Sorted Column 2:", sorted_col2)

difference = 0

for i in range (len(sorted_col1)):
    difference += abs(sorted_col1[i] - sorted_col2[i])

print("Difference:", difference)