from functools import reduce

n = int(input())
m = int(input())

result = 0

inputs = []

for i in str(m):
    inputs.append(int(i))
    result = reduce(lambda acc, value: acc + value, inputs)

print(result)