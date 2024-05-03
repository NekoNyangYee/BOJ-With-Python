while True:
    str = input()

    if str == "END":
        break
    else:
        str = str[::-1]
        print(str)