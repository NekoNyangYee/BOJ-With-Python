n = int(input())

for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    print("*" * (2 * (n - i) + 1))
for j in range(1, n):
    print(" " * (n - j - 1), end="")
    print("*" * (2 * j + 1))