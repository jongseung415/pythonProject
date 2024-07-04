from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

try:
    a = [1,2]
    print(a[3])

    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    with open("logTestFile.txt", "w") as f:
        f.write(f"{current_time} ERROR:{e}")
except IndexError as e:
    print("인덱싱할 수 없습니다.")
    with open("logTestFile.txt", "w") as f:
        f.write(f"{current_time} ERROR:{e}")
finally:
    f.close()