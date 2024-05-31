import math

str = input().split(":")
gcd = math.gcd(int(str[0]), int(str[1]))
print(f"{int(str[0]) // gcd} : {int(str[1]) // gcd}")