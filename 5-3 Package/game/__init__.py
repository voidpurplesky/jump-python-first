'''
__init__.py의 용도
해당 디렉터리가 패키지의 일부임을 알려주는 역할
3.3 버전부터는 없어도 패키지로 인식한다 PEP420 
하지만 하위버전호환을 위해 파일을 생성하는것이 안전
'''
# 패키지 변수 및 함수 정의
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 패키지 내 모듈을 미리 import > game_main.py

from .graphic.render import render_test

# 패키지 초기화
# 데이터베이스 연결이나 설정 파일 로드

# 여기에 패키지 초기화 코드를 작성
print("Initializing game...")