n = int(input())

string = []

for j in range(1, n + 1):
    string = list(map(int, input().split()))
    string = string[1:]
    s_string = sorted(string)
    lg = 0
    for i in range(0, len(s_string) - 1):
        if s_string[i+1] - s_string[i]>lg:
            lg = s_string[i+1] - s_string[i]
    print(f"Class {j}")
    print(f'Max {max(s_string)}, Min {min(s_string)}, Largest gap {lg}')
