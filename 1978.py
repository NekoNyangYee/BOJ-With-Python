n = int(input())

num = list(map(int, input().split()))

lst = []

for i in num:
    if i > 1:
        is_prime = True
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            lst.append(i)
print(len(lst))

