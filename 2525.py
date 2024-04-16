time = ["23", "48", "25"]
h = int(time[0])
m = int(time[1])
after = int(time[2])

if m + after < 60:
    print(h, m + after)
elif m + after >= 120:
    print(h + 2, m + after - 120)
elif m + after >= 60 and h == 23:
    print(24 - (h + 1), m + after - 60)