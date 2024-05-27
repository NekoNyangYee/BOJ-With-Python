n = int(input())

result = 0

while n > 1:
    result += n // 5
    n //= 5

print(result)