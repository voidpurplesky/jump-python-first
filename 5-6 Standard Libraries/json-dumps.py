#json.dumps(dictionary) : 파이썬 자료형을 json 문자열로 

from json import dumps, loads
d = {'name':'홍길동', 'birth':'0525', 'age':30}
json_data = dumps(d)
print(json_data)
#{"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30}

# json>dic
print(loads(json_data))
#{'name': '홍길동', 'birth': '0525', 'age': 30}