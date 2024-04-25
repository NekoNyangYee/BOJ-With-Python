T = int(input())
sum = 0
result = 0
num = list(map(int, input().split()))
for i in range(T):
    if num[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0
    


print(result)