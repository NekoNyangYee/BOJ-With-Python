from sys import stdin

n, k = list(map(int, stdin.readline().split()))

lst = []
people = list(range(1, n + 1))
index = 0

while people:
    index = (index + k - 1) % len(people)
    lst.append(people.pop(index))

print("<", end="")
for i in range(n - 1):
    print(lst[i], end=", ")
print(lst[n - 1], end="")
print(">", end="")
