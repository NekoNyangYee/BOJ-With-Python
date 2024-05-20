n = int(input())

lst = []
even_lst = []

for _ in range(n):
    num = list(map(int, input().split()))
    lst.append(num)
    even_nums = [x for x in num if x % 2 == 0]
    even_lst.append(even_nums)

for i in lst:
    print(sum(even_lst), min(even_lst))