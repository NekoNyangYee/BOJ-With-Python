n = int(input())
print("Gnomes:")

for i in range(n):
    a, b, c = list(map(int, input().split()))
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)

    if sorted(lst, reverse = True) == lst or sorted(lst, reverse = False) == lst:
        print("Ordered")  
    else:
        print("Unordered")