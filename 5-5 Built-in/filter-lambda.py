#filter

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))
#[1,2,6]
def positive(x):
    return x > 0
print(list(filter(positive, [1,-3,2,0,-5,6])))

# filter + lambda
# 양수 x > 0
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))
#[1, 2, 6]
