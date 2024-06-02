n, d = map(int, input().split())

digit = str(d)

count = 0

for i in range(1, n + 1):
    count += str(i).count(digit)

print(count)
