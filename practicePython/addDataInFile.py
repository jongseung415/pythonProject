f = open("newFileOpenByPython.txt", 'a')

for i in range(11,20):
    data = "%d번 째 줄입니다.\n" % i
    f.write(data)
f.close()