def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)

from functools import reduce
result = reduce(lambda x, y: x + y, data)
print(result)

#최대값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)
