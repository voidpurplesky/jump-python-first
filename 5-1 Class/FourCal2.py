class FourCal:
    def __init__(self, num1, num2): # 생성자
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def div(self):
        return self.num1 / self.num2
    
fourCal = FourCal(4, 2)
print(fourCal.num1)
print(fourCal.add())
        

# 상속
class MoreFourCal(FourCal):
    pass

moreFourCal = MoreFourCal(4, 2)
print(moreFourCal.add())
print(moreFourCal.div()) #2.0

