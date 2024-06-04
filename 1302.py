from collections import Counter

n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

counter = Counter(lst)
max_count = max(counter.values())

most_common = [book for book, count in counter.items() if count == max_count]

most_common.sort()
most_common = most_common[0]

print(most_common)