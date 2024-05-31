n = int(input())

for _ in range(n):
    input_str = list(input().split())
    for j in input_str:
        print(j[::-1], end=" ")
