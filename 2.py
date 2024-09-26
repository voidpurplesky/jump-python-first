num1 = 3
num2 = 3.14
num3 = -5
print(num1)
print(num2)
print(num3)
# commant 주석
'''
주석'''
print(type(num1)) # <class 'int'>
print(type(num2)) # <class 'float'>
print(type(num3)) # <class 'int'>


l = [80,75,55]
t = (80,75,55)
d = {'국어':80,'영어':75,'수학':55}
print(d['국어'])

#1
s = sum(t)
print(s)
print(s/len(t))

'''
210
70.0
'''

print(sum(list(d.values())))
print(len(d))
print(sum(list(d.values()))/len(d))