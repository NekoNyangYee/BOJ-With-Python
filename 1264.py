while True:
    sentence = input()
    count = 0
    if sentence == '#':	# 입력의 끝
        break
    for c in sentence:
        if c in 'aeiouAEIOU': # 모음이면
            count += 1
    print(count)