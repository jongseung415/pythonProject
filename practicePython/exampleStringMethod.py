# count()
exampleOne = "my baby bear doll is very cute!"
wordQuantity = exampleOne.count('b')
print(wordQuantity)

# find()
exampleTwo = "Python is the best choice"
wordIndex = exampleTwo.find('P')
notExistWordIndex = exampleTwo.find('D')
print(wordIndex)
# 존재하지 않을 경우 -1을 반환
print(notExistWordIndex)

# index(), find() 내장 함수와의 차이점은 존재하지 않을 경우 오류가 발생
exampleThree = "Life is too short"
indexNumber = exampleThree.index('t')
print(indexNumber)