a, b = input().split()
lst = []
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            cnt += 1
lst.append(cnt)
print(min(lst))