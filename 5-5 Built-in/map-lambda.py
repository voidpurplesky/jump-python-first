
# map
def two_times(numberList):
    result = []
    for i in numberList:
        result.append(i * 2)
    return result

result = two_times([1,2,3,4])
print(result)
#[2, 4, 6, 8]

# 위를 map 사용해서 변경
def two_times(x):
    return x * 2

print(list(map(two_times, [1,2,3,4])))

print(list(map(lambda a: a * 2, [1,2,3,4])))