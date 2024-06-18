# 01
subjectScore = {"korean": 80, "english": 75, "math": 55}

gildongKoreanScore = subjectScore.get("korean")
gildongEnglishScore = subjectScore.get("english")
gildongMathScore = subjectScore.get("math")

gildongAverageScore = (gildongKoreanScore + gildongEnglishScore + gildongMathScore) / 3

print(gildongAverageScore)

# 02
insertedNumber = 13
if (insertedNumber % 2) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 03
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 03-1
splitedPin = pin.split("-")
birthYearMonthDay = splitedPin[0]
pinNumber =splitedPin[1]
print(birthYearMonthDay)
print(pinNumber)

# 04
numberOfSex = pin[7]
print(numberOfSex)

# 05
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 06
listA = [1,3,5,4,2]
listA.sort()
listA.reverse()
print(listA)

# 07
setenceList = ["life", "is", "too", "short"]
result = " ".join(setenceList)
print(result)

# 08
tupleA = (1,2,3)
tupleA = tupleA + (4,)
print(tupleA)

# 09
dicA = dict()
print(dicA)

dicA['name'] = 'python'
print(dicA)
dicA[('a',)] = 'java'
print(dicA)
#dicA[[1]] = "PHP"
#print(dicA)
dicA[250] = "C"
print(dicA)

# 10
dicScore = {'A':90,'B':80,'C':70}
resultScore = dicScore.pop('B')
print(dicScore)
print(resultScore)

# 11
listGroupA = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(listGroupA)
listGroupB = list(aSet)
print(listGroupB)

# 12
a = b = [1,2,3]

resultBoolean = a is b
print(resultBoolean)
print(id(a))
print(id(b))

a[1] = 4
print(b)