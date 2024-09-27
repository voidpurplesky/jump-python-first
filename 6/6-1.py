


def gugu(dan):
    pr = str(dan) + '단('

    for i in range(1,10):
        if i < 9:
            pr += str(dan * i) + ', '
        else:
            pr += str(dan * i) + ')'
        

    print(pr)



#
def gugu2(dan) -> list:
    l = []
    for i in range(1,10):
        l.append(dan * i)

    print(l)

dan = int(input("출력할 단 : "))

gugu(dan)
gugu2(dan)


def gugu3(number):
    result = []
    for i in range(1,10):
        result.append(number * i)
    str1 = ("%s단 : " % number) + (" ".join(map(str,result)))
    #TypeError: sequence item 0: expected str instance, int found
    return str1 

print(gugu3(3))