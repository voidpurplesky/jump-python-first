class FourCal:
    def __init__(self): # 생성자
        self.num1 = 0
        self.num2 = 0

    def __init__(self, num1, num2): # 생성자
        self.num1 = num1
        self.num2 = num2

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
fourCal = FourCal()
fourCal.setdata(4, 2)
print(fourCal.num1)
print(fourCal.add())
        
fourCal2 = FourCal()
print(fourCal2.add()) # 0

