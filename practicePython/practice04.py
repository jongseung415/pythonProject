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

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)