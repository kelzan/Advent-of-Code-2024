def read_int_pairs(file_path):
    pairs = []
    pages = []
    
    with open(file_path, 'r') as file:
        section_one = True
        for line in file:
            # Strip whitespace and check if the line is empty
            line = line.strip()
            if not line:
                section_one = False
                continue  # Stop reading if we encounter a blank line
            
            if (section_one):
                # Split the line by '|' and convert each part to an integer
                try:
                    pair = [int(num) for num in line.split('|')]
                    if len(pair) == 2:  # Ensure we have exactly two numbers
                        pairs.append(tuple(pair))
                except ValueError:
                    # If conversion to int fails, we'll skip this line
                    print("YUPPER")
                    continue
            else: # section two
                plist = [int(num) for num in line.split(',')]
                pages.append(plist)
    return pairs, pages

def find_index(lst, target):
    try:
        # Returns the index of the first occurrence of target
        return lst.index(target)
    except ValueError:
        # If the target is not found, return -1 or handle the exception in another way
        return -1

def test_pages(rules, pagelist):
    for rule in rules:
        first = find_index(pagelist, rule[0])
        second = find_index(pagelist, rule[1])
        #print(f"Checking rule {rule} in {pagelist}. first index {first}, second {second}")
        if ((first == -1) or (second == -1)):
            continue
        if (first < second):
            continue
        else:
            return False
    return True

def fix_pages(rules, pagelist):
    clean = False
    while not clean:
        clean = True
        for rule in rules:
            first = find_index(pagelist, rule[0])
            second = find_index(pagelist, rule[1])
            #print(f"Checking rule {rule} in {pagelist}. first index {first}, second {second}")
            if ((first == -1) or (second == -1)):
                continue
            if (first < second):
                continue
            else:
                dummy = pagelist[first]
                pagelist[first] = pagelist[second]
                pagelist[second] = dummy
                clean = False
                break
        

# Example usage
file_path = 'day5a_input.txt'
rules,pages = read_int_pairs(file_path)
print(rules)
print(pages)

total = 0
for plist in pages:
    if test_pages(rules,plist):
        print(plist, " is good")
        #print(f"middle: {plist[middle]}")
    else:
        print(plist, " is NOT good, reordering")
        fix_pages(rules, plist)
        print(plist, " reordered: ", test_pages(rules,plist))
        middle = len(plist)//2
        total += plist[middle]

print(f"Total: {total}")