n = int(input())

input_str = input()

numbers = [int(num) for num in input_str.split()]

set_num = set(numbers)

list_num = list(set_num).sort()

print(" ".join(map(str, list_num)))