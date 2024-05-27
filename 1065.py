n = int(input())

cnt = 0

for i in range(1, n + 1):
    digits = list(map(int, str(i)))
    if len(digits) <= 2:
        cnt += 1
    else:
        diff = digits[1] - digits[0]
        is_hansu = True
        for j in range(1, len(digits) - 1):
            if digits[j + 1] - digits[j] != diff:
                is_hansu = False
                break
        if is_hansu:
            cnt += 1

print(cnt)