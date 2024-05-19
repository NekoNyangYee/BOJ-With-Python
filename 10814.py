n = int(input())

users = []

for _ in range(n):
    age, name = input().split()
    users.append([int(age), name])

for user in sorted(users, key=lambda x: x[0]):
    print(user[0], user[1])