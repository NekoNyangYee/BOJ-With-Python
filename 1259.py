while True:
    str = input()
    if str == "0":
        break
    
    if str == str[::-1]:
        print("yes")
    else:    
        print("no")

    