a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c

for i in range(10):
    print(str(multiply).count(str(i)))