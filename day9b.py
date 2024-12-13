


def read_file(file_path):

    with open(file_path, 'r') as file:
        for line in file:
            digit_list = [int(char) for char in line]
            break
    return digit_list

def parse_disk_map(disk_map):
    id = 0
    fsize = True
    fs = []
    for file in disk_map:
        if fsize:
            contents = id
            id += 1
            fsize = False
        else:
            contents = -1
            fsize = True
        fs = fs + [contents] * file
    return fs

def compress_sys(fsys):
    while (fsys.count(-1)):
        last_item = fsys.pop()
        first_empty = fsys.index(-1)
        fsys[first_empty] = last_item

def defrag_sys(fsys):
    max_id = max(fsys)
    for x in range(max_id,0,-1):
        # print(f"Processing ID {x}")
        id_index, length = find_id(fsys, x)
        # print(f"ID Index: {id_index}, Length: {length}")
        space = find_contiguous_space(fsys, length)
        # print(f"Space: {space}")
        if ((space == -1) or (space > id_index)):
            continue
        for x in range(length):
            fsys[space+x] = fsys[id_index+x]
            fsys[id_index+x] = -1
        # print(fsys)


def find_contiguous_space(fsys, num):
    numfound = 0
    tracking = False
    for x in range(len(fsys)):
        if fsys[x] == -1:
            if not tracking:
                # print(f"Found empty space at {x}")
                tracking = True
                numfound = 1
                start = x
            else:
                numfound += 1
            if numfound == num:
                # print(f"Found contiguous space at {start}, ending at {x}")
                return start
        else:
            tracking = False
            numfound = 0
    return -1

def find_id(fsys, id):
    id_index = fsys.index(id)
    length = 0
    for x in range(id_index,len(fsys)):
        if (fsys[x] != id):
            break
        else:
            length += 1
    return id_index, length

def get_checksum(fsys):
    cs = 0
    for x in range(len(fsys)):
        if fsys[x] != -1:
            cs = cs + (x*fsys[x])
    return cs

file_path = 'day9a_input.txt'
disk_map = read_file(file_path)
print(disk_map)

fsys = parse_disk_map(disk_map)
print(fsys)

defrag_sys(fsys)
print(fsys)

checksum = get_checksum(fsys)
print(f"Checksum: {checksum}")