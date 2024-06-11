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

# join()
exampleFour = "abcd"
applyJoinMethod = ",".join(exampleFour)
print(applyJoinMethod)

# upper(), lower()
exampleWord = "hi"
applyUpperMethod = exampleWord.upper()
applyLowerMethod = exampleWord.lower()
print(applyUpperMethod)
print(applyLowerMethod)

# strip(), lstrip(), rstrip()
exampleWordHasGap = " hi "
applyStripMethod = exampleWordHasGap.strip()
applylStripMethod = exampleWordHasGap.lstrip()
applyrStripMethod = exampleWordHasGap.rstrip()
print(applyStripMethod)
print(applylStripMethod)
print(applyrStripMethod)

# replace()
applyReplaceMethod = exampleThree.replace("Life", "Your leg")
print(applyReplaceMethod)

# split()
applySplitMethod = exampleThree.split()
print(applySplitMethod)
exampleFive = "dave : 26, john : 11, adams : 41, tylus : 32"
print(exampleFive.split(":"))
