string = list(input())

lst = []

for i in range(len(string)):
    lst.append(string[i:])

lst.sort()

for i in lst:
    print("".join(i))