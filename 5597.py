s = [i for i in range(1, 31)]

for _ in range(28):
    s.remove(int(input()))


print(min(s))
print(max(s))

"""
lst = []

for _ in range(28):
    lst.append(int(input()))

lst.sort()

for i in range(1, 29):
    if i not in lst:
        print(i)
"""
    