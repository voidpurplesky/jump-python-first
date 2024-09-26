#json.load(file_object) : json 파일을 읽어 딕셔너리 자료형으로 리턴
from json import load

with open('5-6 Libraries/json-dump.json', 'r', encoding='utf-8') as f:
    data = load(f)
    print(type(data)) # <class 'dict'>
    print(data)
#{'name': '홍길동', 'birth': '0525', 'age': 30}

