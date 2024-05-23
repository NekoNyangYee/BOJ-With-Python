while True:
    n = input()
    if n == "#":
        break
    val = n[0]
    data = n[2::]
    result = data.count(val) + data.count(val.upper())
    print(val, result)