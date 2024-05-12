str = input()
list = [0] * 26

for i in str:
    list[ord(i) - 97] += 1
    
for i in list:
    print(i, end=' ')