# 문자열 포매팅

# %d는 정수를 입력 받음
exampleStringTwo = "I eat %d apples."
print(exampleStringTwo % 3)

# %s는 문자열을 입력 받음
exampleStringThree = "I eat %s apples."
print(exampleStringThree % "five")

# 변수로도 대입이 가능
exampleNumber = 3
print(exampleStringTwo % exampleNumber)

# 두 개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 쉼표로 구분하여 각각의 값을 넣어준다.
anotherExampleString = "I ate %d apples. so I was sick for %s days."
exampleNumberTwo = 10
day = "Three"
print(anotherExampleString % (exampleNumberTwo, day))

# 일반적으로 자료형에 따라 포맷 코드가 바뀌어야 하지만, %s 포맷 코드에는 어떤 형태의 값이든 문자열로 바꾸어 대입할 수 있다.
# 원래라면 정수를 삽입하려면 %d를 사용해야한다.
anotherExampleStringTwo = "I have %s apples"
print(anotherExampleStringTwo % 3)
# 원래라면 실수를 삽입하려면 %f를 사용해야한다.
anotherExampleStringThree = "rate is %s"
print(anotherExampleStringThree % 3.234)

# 아래 코드는 오류가 발생한다.
# anotherExampleStringFour = "Error is %d%."
# print(anotherExampleStringFour % 98)

# 포매팅 연산자와 함께 문자'%'를 같이 사용하려면 %%와 같은 형식으로 써줘야한다.
anotherExampleStringFive = "Error is %d%%."
print(anotherExampleStringFive % 98)

#포맷 코드와 숫자 함께 사용하기

# 문자열 포맷 코드 %s 사이에 숫자를 집어넣어 길이를 지정하고 문자열이 오른쪽으로 정렬하도록 한다.
greeting = "hi"
print("%10s" % greeting)

# 10의 길이로 왼쪽 정렬
print("%-10sjane" % greeting)