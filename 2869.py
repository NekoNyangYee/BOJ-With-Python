import math

a, b, v = map(int, input().split())

days = math.ceil((v - b) // (a - b))

print(days)