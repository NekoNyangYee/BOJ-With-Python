N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = sum(1 for i in N if i % 42 != 0)
print(result)