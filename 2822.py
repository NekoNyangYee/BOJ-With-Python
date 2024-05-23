lst = []

for _ in range(8):
    n = int(input())
    lst.append(n)

index_score = [(score, index) for (index, score) in enumerate(lst, start=1)]

sorted_index_score = sorted(index_score, key = lambda x: x[0], reverse=True)

top_5_score = sorted_index_score[:5]

top_5_score_index = [index for score, index in top_5_score]
top_5_score_sum = [score for score, index in top_5_score]

top_5_score_index.sort()

print(sum(top_5_score_sum))
print(" ".join(map(str, top_5_score_index)))