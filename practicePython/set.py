# set은 집합 자료형이라고 한다.
# set() 키워드로 사용해 만들 수 있다.
# 리스트나 문자열 자료형의 값만 할당할 수 있다.
s1 = set([1,2,3])
print(s1)
# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다.

# 리스트나 튜플은 순서가 있기 떄문에 인덱싱을 통해 요솟값을 얻을 수 있지만,
# 집합 자료형은 순서가 없기 때문에 인덱싱을 통해 요솟값을 얻을 수 없다.
# 다만, 집합 자료형에 저장된 값을 인덱싱으로 접근하려면, 리스트나 튜플로 전환하여 사용할 수 있다.
l1 = list(s1)
print(l1[0])

t1 = tuple(s1)
print(t1[0])

#교집합, 합집합, 차집합을 구하는데, 집합 자료형을 유용하게 사용할 수 있다.
s2 = set([1,2,3,4,5,6])
s3 = set([4,5,6,7,8,9])

#교집합 &나 intersectiont() 함수를 이용해서 교집합을 구할 수 있다.
result1 = s2 & s3
print(result1)
result1_1 = s2.intersection(s3)
print(result1_1)

# 합집합 |나 union() 함수를 이용해서 교집합을 구할 수 있다.
result2 = s2 | s3
print(result2)
result2_1 = s2.union(s3)
print(result2_1)

# 차집합 -나 difference() 함수를 이용해서 차집합을 구할 수 있다.
result3 = s2 - s3
print(result3)
result3_1 = s3 - s2
print(result3_1)
result4 = s2.difference(s3)
print(result4)
result4_1 = s3.difference(s2)
print(result4_1)

# add(), update()
s4 = set([1,2,3,4,5])
s4.add("six")
print(s4)
s4.update(["seven", 8, 9])
print(s4)

# remove()
s4.remove("seven")
print(s4)