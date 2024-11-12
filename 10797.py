n = int(input())
count = 0
car_num = list(map(int, input().split())) 
for i in car_num:
    
    if i == n:
        count += 1
print(count)