import sys

n = int(input())

inputs = []

for _ in range(n):
    number = int(sys.stdin.readline())
    inputs.append(number)

inputs.sort()

for num in inputs:
    print(num)