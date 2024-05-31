import math

str1 = input()
str2 = input()
lcm = math.lcm(len(str1), len(str2))

extended_a = str1 * (lcm // len(str1))
extended_b = str2 * (lcm // len(str2))

if extended_a == extended_b:
    print(1)
else:
    print(0)