n = int(input())
count = 0

for i in range(5):
    car_num = list(map(int, input().split())) 
    if car_num[i] == n:
        count += 1
print(count)