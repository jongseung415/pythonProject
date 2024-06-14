dic = {"ItisNumber": 123, "ItisString":"IamString", "ItisList":[1,2,3]}

# 딕셔너리 쌍 추가, 삭제
dictionaryConstruct = dic.items()
print(dictionaryConstruct)

dic["ItisTuple"] = (1,)
print(dictionaryConstruct)

del dic["ItisNumber"]
print(dictionaryConstruct)

iWantToChoose = dic["ItisTuple"]
print(iWantToChoose)


# 딕셔너리에서 key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들은 모두 무시된다는 점에 주의해야 한다.
# key 자리에 리스트 헝태는 쓸 수 없다는 것

keys = list(dic.keys())
values = dic.values()
print(keys)
print(values)

iWantToChooseToo = dic.get('ItisTuple')
print(iWantToChooseToo)
ifNokeyToUseGet = dic.get('noKey', "IamDefault") # get 함수를 사용할 때는 없는 키값을 호출하게 되면 일반적으로는 'None' 값이 리턴되지만, 디폴트 값을 지정할 경우 지정한 디폴트 값이 반환된다.
print(ifNokeyToUseGet)
# ifNokeyToUseKey = dic['nokey'] get 함수를 사용할 때와 달리 오류가 발생한다.
# print(ifNokeyToUseKey)

chkIndic = 'ItisTuple' in dic
print(chkIndic)