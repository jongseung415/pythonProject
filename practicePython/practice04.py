# 01
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


if is_odd(3):
    print("홀수")
else:
    print("짝수")


# 02
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print(result / len(args))


avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)

# 05
# f1 = open("test.txt", "w")
# f1.write("Life is too short")
# f1.close()
#
# f2 = open("test.txt", "r")
# f2Content = f2.readline()
# print(f2Content)
# f2.close()

# 07
# f = open('test.txt', 'r')
# body = f.read()
# f.close()
# body = body.replace("java", "python")
# f = open('test.txt', 'w')
# f.write(body)
# f.close()

# 08
import sys

myargv = sys.argv[1:]


def sumMyargvs(myargv):
    result = 0
    for argv in myargv:
        result += int(argv)
    return result


print(sumMyargvs(myargv))
