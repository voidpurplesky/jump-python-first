#2-2 문자열 자료형
# str() 함수가 있으므로 변수명으로 str을 쓰지말것!

str1 = "str"

str2 = """str'"""
print(str2)
str2 = """str" """
print(str2)
str1 = ''''str'''
print(str1)
str1 = ''''str' '''
print(str1)
str1 = ''''str'
'''
print(str1)

print("-" * 50)

str1 = "0123456789"
print(len(str1))
#print(str1[10]) # IndexError: string index out of range
print(str1[0:1]) # 0
print(str1[5:7]) # 0

pin = "240925-1234567"
print(pin[0:6])
print(pin[7:14])
print(pin[7:8])
# 문자열 포매팅
# 자바처럼 1+"str" 불가

print("%d입니다." % 3)
print("%s입니다." % 3)
num = 3
str1 = "입니다."
str2 = "%d%s" % (num, str1)
print("%d%s" % (num, str1))
print(str2)
str2 = str(num) + str1
print(str2)
print("%0.4f" % 0.1234567) # 0.1235


pr = "string" + str(1)
print(pr)

s = ("a") + ("b")
print(s)