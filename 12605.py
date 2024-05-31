n = int(input())
lst = []

for i in range(1, n + 1):
    input_str = input().split()
    input_str.reverse()
    lst.append(input_str)

for i, line in enumerate(lst, start=1):
    join_line = " ".join(line)
    print(f"Case #{i}: {join_line}")