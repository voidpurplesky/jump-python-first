class Family:
    #클래스변수 : 클래스가 만들어질때
    lastname = "김"

    #객체변수: 객체생생될때
    def __init__(self):
        self.firstname = "가가"

a = Family()
b = Family()
Family.lastname = "박"
print(a.lastname)
print(a.firstname)
a.lastname = "이"
print(a.lastname)