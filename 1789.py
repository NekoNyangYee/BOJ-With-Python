s = 200
current = 1
total_sum = 0

while True:
    total_sum += current
    if total_sum > s:
        break
    current += 1

max_num = current - 1

print(max_num)