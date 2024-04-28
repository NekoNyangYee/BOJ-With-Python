from functools import reduce

n = 25
m = 7000000000000000000000000

result = 0

inputs = []

for i in str(m):
    inputs.append(int(i))
    result = reduce(lambda acc, value: acc + value, inputs)

print(result)