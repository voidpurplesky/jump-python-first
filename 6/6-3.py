# 6-3 게시판 페이징하기 312
'''
게시물의 총 개수(m) | 페이지당 보여줄 게시물수(n) | 총페이지수
5                   | 10                        | 1
15                  | 10                        | 2
25                  | 10                        | 3
30                  | 10                        | 3
'''
def get_total_page(m, n):
    result = m // n 
    if m % n > 0: result = result + 1
    print(result)

get_total_page(25, 10)
get_total_page(30, 10)