#if
money = True

if money:
    print("taxi")
else:
    print("walk")

print(1 in [1,2,3]) #T
print(1 in (1,2,3))
print('1' in '123')

l = ['a', 'b', 'c']
if 'a' in l:
    print('a in list')


if 'd' in l:
    pass
elif 'a' in l:
    print('a in list')

# 조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
print(message)
