a = [1,2,3,4,5]

# append()
a.append(6) # 리스트의 맨 마지막에 매개변수 값을 추가한다.
print(a)

# sort()
a = [1,7,16,38,99,65]
a.sort() # 현재의 리스트를 순서대로 정렬
print(a)

# reverse()
names = ["adam", "song", "wheel", "casey", "ben", "polo"]
names.reverse() # 현재의 리스트를 그대로 거꾸로 뒤집는다.
print(names)
names.sort()
print(names)

names.reverse()
print(names)

# index()
namesIndexNumber = names.index("polo") # index() 함수는 매개변수와 동일한 값의 인덱스 값을 리턴한다.
print(namesIndexNumber)

# insert()
a.insert(6,100) # insert()함수에서 첫번째 매개변수는 인덱스 값을 의미하고 두번째 매개변수는 입력할 값을 의미한다.
print(a)

# remove()
x = [1,2,3]
x = x * 3
print(x)
x.remove(1) # remove() 함수의 매개변수 값은 특정 값을 의미한다. remove() 함수는 리스트에서 매개변수값과 동일한 값 중 제일 처음에 나오는 값을 삭제한다.
print(x)

# pop()
popOutObject = x.pop() # 매개변수 값을 주지 않으면 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
print(popOutObject)
print(x)

popOutObject = x.pop(2) # pop() 함수의 매개변수 값은 x번째 요소를 의미한다.
print(popOutObject)
print(x)

# count()
countsNumberTwo = x.count(2) # count() 함수는 리스트 안에서 매개변수 값과 같은 값의 수를 리턴한다.
countsNumberThree = x.count(3)
print(countsNumberTwo)
print(countsNumberThree)

# extend()
print(x)
x.extend([10,11]) # extend() 함수의 매개변수로는 리스트 형태만 올 수 있고, 함수를 적용할 대상 리스트에 매개변수 리스트를 더하게 된다.
print(x)