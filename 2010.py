n = int(input())

sum = 1

for _ in range(n):
    s = int(input())
    sum += s
    
sum_plug = sum - n

print(sum_plug)