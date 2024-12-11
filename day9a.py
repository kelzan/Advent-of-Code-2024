


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

def get_checksum(fsys):
    cs = 0
    for x in range(len(fsys)):
        cs = cs + (x*fsys[x])
    return cs

file_path = 'day9a_input.txt'
disk_map = read_file(file_path)
print(disk_map)

fsys = parse_disk_map(disk_map)
print(fsys)

compress_sys(fsys)
print(fsys)

checksum = get_checksum(fsys)
print(f"Checksum: {checksum}")