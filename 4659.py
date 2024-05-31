def is_acceptable(s):
    vowels = "aeiou"
    
    # 조건 1: 모음이 하나 이상 포함되어야 한다.
    has_vowel = any(char in vowels for char in s)
    if not has_vowel:
        return False
    
    # 조건 2: 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    vowel_count = 0
    consonant_count = 0
    
    for i in range(len(s)):
        if s[i] in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        if vowel_count == 3 or consonant_count == 3:
            return False
    
    # 조건 3: 같은 글자가 연속적으로 두 번 오면 안 되지만, 'ee'와 'oo'는 허용.
    for i in range(1, len(s)):
        if s[i] == s[i-1] and s[i] not in "eo":
            return False
    
    return True

lst = []

while True:
    str = input()
    if str == "end":
        break
    lst.append(str)

for line in lst:
    if is_acceptable(line):
        print(f"<{line}> is acceptable.")
    else:
        print(f"<{line}> is not acceptable.")