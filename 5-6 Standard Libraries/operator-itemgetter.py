# sorted 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할수 있게 도와주는 모듈

from operator import itemgetter
# tuple
students = [
    ('jane', 22, 'A'),
    ('dave', 32, 'B'),
    ('sally', 17, 'B')
]

result = sorted(students, key=itemgetter(1)) # 0 name 1 age 2 grade
print(result)
#[('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

# dictionary
students = [
    {"name":"jane", "age": 22, "grade":"A"},
    {"name":"dave", "age": 32, "grade":"B"},
    {"name":"sally", "age": 17, "grade":"B"}
]

result = sorted(students, key=itemgetter('age'))
print(result)
#[{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]


