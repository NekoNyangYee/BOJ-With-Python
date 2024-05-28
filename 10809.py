S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')


"""s = input()

default_alphabet = [-1] * 26

for i in range(len(s)):
    if default_alphabet[ord(s[i]) - 97] == -1:
        default_alphabet[ord(s[i]) - 97] = i

print(default_alphabet)"""