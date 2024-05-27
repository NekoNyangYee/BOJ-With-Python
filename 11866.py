from sys import stdin

n, k = map(int, stdin.readline().split())

people = list(range(1, n + 1))
result = []
index = 0

while people:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index))

print("<",end="")
for i in range(n - 1):
    print(result[i],end=", ")
print(result[n - 1], end = "")
print(">",end="")