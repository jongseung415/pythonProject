# f 문자열 포매팅, 3.6 버전 이상 부터 사용 가능
name = "jane"
age = 36
print(f"I am {name}. my age is {age}.")

# 표현식을 지원하기 때문에 연산 처리도 가능
print(f"I am {name}. my age is {age + 1}.")

# 딕셔너리 사용 가능
dictionaryKeyValue = {'name':'jane','age':32}
print(f"my name is {dictionaryKeyValue['name']}. my age is {dictionaryKeyValue['age'] + 1}.")

greeting = "hi"

print(f"{greeting:!<10} user, welcome!")

print(f"{greeting:>10}")

print(f"{greeting:^10}")