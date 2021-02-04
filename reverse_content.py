# Python Program to Reverse the Content of a File using Stack

import os


class Stack:

    def __new__(cls, *args, **kwargs):
        return super(Stack, cls).__new__(cls)

    def __init__(self):
        self.arr = []

    def push(self, val):
        return self.arr.append(val)

    def is_empty(self):
        return len(self.arr) == 0

    def pop(self):
        if self.is_empty():
            print("Array is empty")
            return
        return self.arr.pop()


def reverse_file_content(filename):
    s = Stack()
    original = open(filename)
    for lines in original:
        s.push(lines.rstrip("\n"))
    original.close()
    fil = open(os.path.abspath(original.name), 'w')
    while not s.is_empty():
        fil.write(s.pop() + "\n")
    fil.close()


filename = "GFG.txt"
reverse_file_content(filename)
with open(filename) as f:
    for i in f:
        print(i, end="")
