num = 5
result = 0
hab = 0

for i in range(1, num+1):
    result += i

hab = sum(i**3 for i in range(1, num+1))

print(result)
print(result ** 2)
print(hab)