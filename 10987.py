str = list(input())

count = 0
moum = ['a', 'e', 'i', 'o', 'u']

# 각 모음의 카운트를 저장할 딕셔너리 초기화
moum_count = {key: 0 for key in moum}

# 문자열을 순회하며 각 모음의 개수 카운트
for char in str:
    if char in moum:
        moum_count[char] += 1

total_count = sum(moum_count.values())

print(total_count)