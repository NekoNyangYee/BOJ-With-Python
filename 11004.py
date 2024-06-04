n, k = map(int, input().split())
lst = []
num = list(map(int, input().split()))
for i in num:
    lst.append(i)

lst.sort()

print(lst[k-1])
