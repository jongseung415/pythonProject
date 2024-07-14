def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times_map(x):
    return x * 2

print(list(map(two_times_map, [1,2,3,4])))

print(list(map(lambda a: a * 2,[1,2,3,4])))