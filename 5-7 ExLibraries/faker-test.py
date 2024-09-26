from faker import Faker
fake = Faker()
print(fake.name())
#Chelsey Spence

fake = Faker('ko-KR')
print(fake.name())
#김춘자

print(fake.address())
#부산광역시 중랑구 개포698거리 (지훈김읍)

# 이름과 주소를 쌍으로 하는 30건의 테스트데이터
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)

print(fake.postcode()) # 15799
print(fake.country()) # 슬로베니아
print(fake.company()) # 안하안
print(fake.job()) # 방문 판매원
print(fake.phone_number()) # 062-265-7614
print(fake.user_name()) #dgim
print(fake.text())
'''
Aspernatur exercitationem recusandae doloremque. Nemo veniam unde voluptate dignissimos itaque magnam.
Id commodi magnam eaque similique suscipit.
'''
print(fake.color_name()) #Azure