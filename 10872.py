n = int(input())

sum = 1

for i in range(n, 0, -1):
    sum *= i

print(sum)