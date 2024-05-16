n = list(map(int, input().split()))

count = n.count(1)

if count == 1:
    print("A")
elif count == 2:
    print("B")
elif count == 3:
    print("C")
else:
    print("D")