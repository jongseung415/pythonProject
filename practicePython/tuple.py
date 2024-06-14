# tuple
# 리스트는 [], 튜플은 ()으로 둘러싼다.
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.

t1 = ()
t2 = (1,) # 단지 1개의 요소만을 가질 때는 요소 뒤에 쉼표(,)를 반드시 붙여야 한다
t3 = (1,2,3)
t4 = 1,2,3 # 튜플 선언 시 소괄호를 생략해도 된다
t5 = ('a','b',('ab','cd'))

indexing = t5[2][1]
print(indexing)

slicing = t5[2][0:1]
print(slicing)

merge = t2 + t4
print(merge)

multi = t4 * 3
print(multi)

length = len(t4)
print(length)