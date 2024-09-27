'''
list(tuple)

'''
from faker import Faker
from random import random
from operator import itemgetter

fake = Faker('ko-KR')
print(fake.name())

# xx.xx
print("\n xx.xx")
print(round(random() * 10, 2)) # 9.99

l = []

for i in range(20):
    l.append((fake.name(), round(random() * 10, 2)))

print(l)

'''
[('이수진', 8.88), ('김은영', 5.36), ('강상철', 3.93), ('차정수', 3.6), ('이예은', 8.6), ('류정호', 6.2), ('이우진', 9.4), ('한정훈', 9.11), ('안상철', 6.9), ('박지영', 8.03), ('고서연', 1.29), ('박정숙', 8.63), 
('이은서', 3.01), ('엄도윤', 8.88), ('이지연', 9.83), ('이승현', 8.18), ('장종수', 0.32), ('박진호', 2.91), ('이채원', 1.94), ('백경희', 9.87)]
'''

result = sorted(l, key=itemgetter(1))
print(result)
'''
[('이지현', 0.07), ('김명숙', 0.49), ('김재호', 1.07), ('김지연', 1.36), ('김경희', 2.44), ('지은주', 2.67), ('김정식', 2.94), ('우현숙', 3.61), ('박민준', 4.61), ('김예준', 5.07), ('이영환', 5.47), ('박서현', 5.5), ('배경수', 5.68), ('이동현', 5.96), ('한수진', 6.17), ('김현정', 6.33), ('김지연', 6.45), ('강유진', 8.31), ('윤정훈', 9.09), ('김지후', 9.23)]
'''

l.sort()
print(l)
'''
[('강지아', 2.64), ('고미정', 1.51), ('김광수', 2.07), ('김명자', 1.73), ('김재호', 9.08), ('박영호', 0.76), ('박은주', 6.35), ('박현정', 9.95), ('손서준', 8.77), ('송준서', 4.0), ('이영숙', 9.26), ('이현숙', 0.5), ('정정숙', 8.57), ('조은정', 7.65), ('최채원', 6.49), ('한순자', 9.9), ('한우진', 3.15), ('한정훈', 8.23), ('홍예지', 3.83), ('황수빈', 6.13)]
'''