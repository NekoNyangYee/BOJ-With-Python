n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * (n - (n - i)) - 1))