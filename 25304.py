total = 260000

result = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    result += int(a) * int(b)

if total == result:
        print("Yes")
else:
    print("No")