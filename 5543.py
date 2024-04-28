burger = []
drink = []
for i in range(0, 3):
    a = int(input())
    burger.append(a)
 
for i in range(0, 2):
    b = int(input())
    drink.append(b)
 
print(min(burger)+min(drink)-50)