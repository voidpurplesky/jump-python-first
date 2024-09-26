#json.dump(dictionary, file_object) : 딕셔너리 자료형을 json파일로 생성 dic>json file
from json import dump

data = {'name':'홍길동', 'birth':'0525', 'age':30}
with open('5-6 Libraries/json-dump.json', 'w', encoding='utf-8') as f:
    dump(data, f, ensure_ascii=False)