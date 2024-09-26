#클래스 객체 attrgetter()
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return str((self.name, self.age))
        
students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B')
]

result = sorted(students, key=attrgetter('age'))
print(result)
#[<__main__.Student object at 0x0000025794F5ADB0>, <__main__.Student object at 0x0000025794F5A3F0>, <__main__.Student object at 0x0000025794F5A4E0>]

for i in result:
    print(i)

'''
sally
jane
dave
'''

for i in result:
    print(i.name, i.age, i.grade)
'''
sally 17 B
jane 22 A
dave 32 B
'''