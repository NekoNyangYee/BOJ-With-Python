import sys
input=sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst) / len(lst)))#1) 산술평균
print(lst[len(lst) // 2])
dic=dict()
for i in lst:#빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())#빈도수 중 최대값 구하기
mx_dic=[]#최빈값 숫자를 저장할 배열

for i in dic:#빈도수 딕셔너리에서
    if mx==dic[i]:#최빈값의 key저장
        mx_dic.append(i)

if len(mx_dic)>1:#최빈값이 여러개라면
    print(mx_dic[1])#두번째로 작은 값  3)최빈값
else:#하나라면
    print(mx_dic[0])#해당 값 출력  3)최빈값
print(max(lst) - min(lst))