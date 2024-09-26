# sympy

# pip install sympy
'''

PS ...> pip install sympy


'''


from fractions import Fraction # 유리수 연산에 사용
from sympy import symbols, Eq, solve

x = symbols("x") # 미지수를 나타내는 기호 x 생성
f = Eq(x * Fraction('2/5'), 1760) # x * (2/5) = 1760

print(f) # Eq(2*x/5, 1760)

# Fraction : 유리수 연산에 사용
# Fraction(분자, 분모)
print(Fraction(1, 5)) # 1/5

# Fraction ('분자, 분모')
print(Fraction('1 / 5')) # 1/5

print(solve(f)) #[4400] x = 4400

# 2차 방정식 x^2 = 1
x = symbols("x")
f = Eq(x**2, 1)
print(solve(f)) #[-1, 1]

# 연립방정식의 해
'''
x + y = 10
x - y = 4
'''
x, y = symbols('x y')
f1 = Eq(x + y, 10)
f2 = Eq(x - y, 4)
print(solve([f1, f2]))