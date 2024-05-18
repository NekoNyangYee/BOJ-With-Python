n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

a_set = set(a)

result = ["1" if i in a_set else "0" for i in b]

print("\n".join(result))    