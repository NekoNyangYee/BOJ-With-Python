n = int(input())
res = 0

for i in range(1, n + 1):
    cnt = i + sum(map(int, str(i)))
    if (cnt == n):
        res = i
        break

print(res)