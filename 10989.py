import sys

n = int(input())

lst = []

for _ in range(n):
    str = int(sys.stdin.readline())
    lst.append(str)

lst.sort()

for num in lst:
    print(num)