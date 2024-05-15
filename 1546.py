n = int(input())

num = list(map(int, input().split()))

lst = []

for i in num:
    lst.append(i / max(num) * 100)

print(sum(lst) / n)