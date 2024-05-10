a, b = map(int, input().split())

s = int(input())

if a + b < s * 2:
    print(a + b)
else:
    print((a + b) - (s * 2))