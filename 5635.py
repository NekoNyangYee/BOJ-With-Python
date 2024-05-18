from datetime import datetime

n = int(input())

people = []

for _ in range(n):
    birth = input().split()
    name = birth[0]
    day = list(map(int, birth[1:]))  # 연, 월, 일을 정수로 변환하여 저장
    birthday = datetime(day[2], day[1], day[0])  # 연, 월, 일을 datetime 객체로 생성
    people.append((name, birthday))

people.sort(key=lambda x: x[1])

oldest_person = people[0]
youngest_person = people[-1]

print(youngest_person[0])
print(oldest_person[0])