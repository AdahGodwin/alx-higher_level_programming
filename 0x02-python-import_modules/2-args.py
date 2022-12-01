#!/usr/bin/python3
from sys import argv

n = len(argv)
index = 1
if n == 1:
    print(f"0 argument.")
elif n == 2:
    print(f"{n-1:d} argument:")
    print(f"{index:d}: {argv[index]:s}")
elif n > 2:
    print(f"{n-1} arguments:")
    for j in range(1, n):
        print(f"{index:d}: {argv[index]:s}")
        index += 1
