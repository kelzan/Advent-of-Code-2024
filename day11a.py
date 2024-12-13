"""The ancient civilization on Pluto was known for its ability to manipulate spacetime, and while The 
Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.

At first glance, they seem like normal stones: they're arranged in a perfectly straight line, and each 
stone has a number engraved on it.

The strange part is that every time you blink, the stones change.

Sometimes, the number engraved on a stone changes. Other times, a stone might split in two, causing all 
the other stones to shift over a bit to make room in their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, 
the stones each simultaneously change according to the first applicable rule in this list:

- If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
- If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
  The left half of the digits are engraved on the new left stone, and the right half of the digits are 
  engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
- If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied 
  by 2024 is engraved on the new stone."""
from collections import deque
from typing import List, Tuple

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("Previous node cannot be null")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def delete(self, node):
        if not self.head or not node:
            return
        if self.head == node:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self.tail = node.prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def initialize_from_array(self, array: List[int]):
        for item in array:
            self.append(item)

def read_initial(file_path):
    """Read the initial state from the specified file. Returns a list of integers."""
    with open(file_path, 'r') as file:
        return [int(number) for number in file.readline().strip().split()]

def blink(rocks: DoublyLinkedList):
    """Simulate a blink."""
    current = rocks.head
    while current:
        next_node = current.next
        if current.data == 0:
            rocks.insert(current, 1)
            rocks.delete(current)
        elif len(str(current.data)) % 2 == 0:
            # print(f"Splitting {current.data}")
            number_str = str(current.data)
            half = len(number_str) // 2
            left = int(number_str[:half])
            right = int(number_str[half:])
            rocks.insert(current, left)
            rocks.insert(current.next, right)
            rocks.delete(current)
        else:
            rocks.insert(current, current.data * 2024)
            rocks.delete(current)
        current = next_node

file_path = "day11a_input.txt"
initial_rocks = read_initial(file_path) 
print(initial_rocks)
# Create a doubly linked list named rocks and initialize it with the initial_rocks
rocks = DoublyLinkedList()
rocks.initialize_from_array(initial_rocks)
rocks.print_list()
# Simulate 10 blinks
for x in range(25):
    blink(rocks)
    print(f"Blink {x+1}, number of rocks: {rocks.count()}") 
    # rocks.print_list()

# print(f"Number of rocks: {rocks.count()}")