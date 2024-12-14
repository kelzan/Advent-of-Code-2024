import re
# Constants
# Cost in tokens per button press
BUTTON_A_COST = 3
BUTTON_B_COST = 1
PRIZE_OFFSET = 10000000000000

def parse_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        content = file.read()
        entries = content.strip().split('\n\n')
        for entry in entries:
            lines = entry.split('\n')
            button_a = re.findall(r'X\+(\d+), Y\+(\d+)', lines[0])[0]
            button_b = re.findall(r'X\+(\d+), Y\+(\d+)', lines[1])[0]
            prize_loc = re.findall(r'X=(\d+), Y=(\d+)', lines[2])[0]
            data.append({
                'button_a': {'x': int(button_a[0]), 'y': int(button_a[1])},
                'button_b': {'x': int(button_b[0]), 'y': int(button_b[1])},
                'prize_loc': {'x': int(prize_loc[0])+PRIZE_OFFSET, 'y': int(prize_loc[1])+PRIZE_OFFSET}
            })
    return data

def format_data(data):
    formatted_entries = []
    for entry in data:
        button_a = entry['button_a']
        button_b = entry['button_b']
        prize_loc = entry['prize_loc']
        formatted_entries.append(
            f"Button A: X+{button_a['x']}, Y+{button_a['y']}\n"
            f"Button B: X+{button_b['x']}, Y+{button_b['y']}\n"
            f"Prize: X={prize_loc['x']}, Y={prize_loc['y']}\n"
        )
    return '\n'.join(formatted_entries)

def win_prize(prize):
    """Find the lowest cost to win the prize. Return the cost, or 0 if it's impossible."""
    a = 0 # a presses
    b = 0 # b presses
    ax = prize['button_a']['x']
    ay = prize['button_a']['y']
    bx = prize['button_b']['x']
    by = prize['button_b']['y']
    px = prize['prize_loc']['x']
    py = prize['prize_loc']['y']

    b = ((ax*py) - (ay*px)) // ((ax*by) - (ay*bx))
    print(f"b: {b}")
    a = (px - (b * bx)) // ax
    print(f"a: {a}")
    if (a * ax) + (b * bx) == px and (a * ay) + (b * by) == py:
        return (a * BUTTON_A_COST) + (b * BUTTON_B_COST)
    return 0


# Example usage
filepath = 'day13a_input.txt'
parsed_data = parse_file(filepath)
print(format_data(parsed_data))

total_cost = 0  # Total cost to win all prizes
for prize in parsed_data:
    cost = win_prize(prize)
    print(f"Cost to win prize at {prize['prize_loc']['x']},{prize['prize_loc']['y']}: {cost}")
    total_cost += cost

print(f"Total cost to win all prizes: {total_cost}")