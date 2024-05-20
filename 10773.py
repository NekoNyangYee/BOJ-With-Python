n = int(input())

lst = []

for _ in range(n):
    num = int(input())
    if num == 0 and lst:  # num이 0이고 lst가 비어있지 않은 경우
        lst.pop()  # 가장 최근에 추가된 요소 삭제
    else:
        lst.append(num)  # num이 0이 아니면 리스트에 추가

print(lst)