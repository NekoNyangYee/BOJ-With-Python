n = int(input())

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (i + 1))
for i in range(n - 1):
    print(" " * (i + 1), end="")
    print("*" * (n - i - 1))