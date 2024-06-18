# 연산자 in, not in

pocket = ['paper', 'cellphone', 'money', 'card']
if 'card' in pocket:
    print("Take a bus!")
else:
    print("Let's walk!")

if 'card' in pocket:
    pass
else:
    print("Stop! Right there!")

# 조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
print(message)