a = 0
while a < 10:
    if a % 3 == 0:
        a += 1
        continue
    else:
        print(a)
        a += 1