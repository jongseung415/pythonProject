# format 함수를 사용하여 포맷팅
exampleSentence = "I eat {0} apples."
print(exampleSentence.format(3))

# format 함수의 경우 문자열 포맷 코드와 달리 {}안의 인덱스 순서대로 데이터 형식에 관계없이 입력된다.
print(exampleSentence.format("five"))

number = 10
print(exampleSentence.format(number))

# 두 개 이상의 값 입력
exampleSentenceTwo = "I ate {0} apples. so I was sick for {1} days."
days = "three"
print(exampleSentenceTwo.format(number,days))

# format 함수를 사용할 때, 인덱스 항목 대신 이룸 항목을 형태를 사용할 수도 있다.
# 이 때 주의 할 점은, format() 함수 안의 값이 'name=value'와 같은 형태로 입력되어야 한다.
exampleSentenceThree = "I ate {number} apples. so I was sick for {day} days."
print(exampleSentenceThree.format(number=3,day="five"))

# 인덱스와 이름 형식을 혼용해서 사용할 수도 있다.
exampleSentenceFour = "I ate {0} apples. so I was sick for {day} days."
print(exampleSentenceFour.format(11,day="one"))

# 정렬 방식
greeting = "hi"
# 우측 정렬
print("{0:>10}".format(greeting))
# 좌측 정렬
print("{0:<10}Jon".format(greeting))
# 가운데 정렬
print("{0:^10}".format(greeting))

# 공백 채우기
greetingTwo = "hello"
print('{0:=^20}'.format(greetingTwo))
print('{0:!^20}'.format(greetingTwo))

# 소수점 표현
x = 3.42134234
print("{0:0.4f}".format(x))
print("{0:!^10.4f}".format(x))