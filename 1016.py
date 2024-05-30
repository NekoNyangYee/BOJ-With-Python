def is_square_free(n):
    # n이 1보다 큰 제곱수로 나누어 떨어지는지 확인
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return True
lst = []
min, max = map(int, input().split())

for i in range(min, max + 1):
    if is_square_free(i):
        lst.append(i)

print(len(lst))
"""min, max = map(int, input().split())


real_count_lst = []

for i in range(min, max + 1):
    tmp = i ** 0.5
    if i == 1:
        continue
    elif round(tmp, 1) == tmp:
        lst.append(i)
    for j in lst:
        if i % j == 0:
            real_count_lst.append(i)

print(len(str(max)) - len(str(real_count_lst)))"""