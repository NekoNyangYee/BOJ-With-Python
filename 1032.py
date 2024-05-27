n = int(input())

strings = []

for _ in range(n):
    strings.append(input())

result = list(strings[0])

for s in strings[1:]:
    for i in range(len(result)):
        if result[i] != s[i]:
            result[i] = '?'
print(''.join(result))