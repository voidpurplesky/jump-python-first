#되새김문제 295
class Calc:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

a = Calc()
a.add(7)
print(a.value)

class UpgradeCalc(Calc):
    def minus(self, val):
        self.value -= val

child = UpgradeCalc()
child.add(7)
print(child.value)
child.minus(4)
print(child.value)

# 클래스 상속 받고 메서드 추가하기 2
# 객체변수가 100이상의 값은 가질수없도록 제한하는 클래스를 만들어

class MaxLimitCalc(Calc):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

child2 = MaxLimitCalc()
child2.add(50)
print(child2.value)
child2.add(60)
print(child2.value) # 100