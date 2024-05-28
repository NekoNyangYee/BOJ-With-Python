n = int(input())

for j in range(n - 1):
    print(" " * (n - j - 1), end="")
    print("*" * (2 * j + 1))
    
for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    print("*" * (2 * (n - i) + 1))
