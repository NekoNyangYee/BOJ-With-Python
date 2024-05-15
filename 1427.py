n = input()

lst = [int(i) for i in n]
sorted_lst = sorted(lst, reverse = True)

result = ''.join(str(num) for num in sorted_lst)

print(result)