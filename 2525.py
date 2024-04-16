# 1. 시간, 분을 먼저 받아오기
H, M = map(int, input().split())
# 2. 더할 시간을 받아오기
timer = int(input()) 

# 3. 받아온 타이머에 60을 나눈 몫을 H에, 60을 나눈 나머지를 M에 더하기
H += timer // 60
M += timer % 60

# 4. M이 60이상이면 H에 1을 더하고 M에서 60을 빼기, H가 24이상이면 H에서 24를 빼기
if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)