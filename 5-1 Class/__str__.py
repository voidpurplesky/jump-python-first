class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        #result = self.name, 
        #result = ",".join((self.name, str(self.age), self.grade))
        result = f'name={self.name}, age={self.age}, grade={self.grade}'
        return result
        #return self.name#,self.age, self.grade
    #TypeError: __str__ returned non-string (type tuple)
a = Student('jane', 22, 'A')
print(a)
#jane,22,A
# name=jane, age=22, grade=A