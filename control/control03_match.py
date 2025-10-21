# match ~ case if와 다르게 케이스로 점프해서 소모자원을 줄여준다

a = input("1 ~3 사이의 정수값을 입력 해 주세요 :")

match a:
    case "1" :
        print("one")
    case "2" :
        print("two")
    case "3" :
        print("three")

season = input("월 입력")

match int(season) :
    case 12 | 1 | 2 :
        print("겨울")
    case 3 | 4 | 5 :
        print("봄")
    case 6 | 7 | 8 :
        print("여름")
    case 9 | 10 | 11 :
        print("가을")
    case _ :
        print(" 1 ~ 12 사이의 값을 입력해주세요!")

# _ : 특별히 값을 사용하고 싶진 않은데, 변수가 필요할떄 사용한다.

values = 1, 2, 3
a, _, b = values
print(a, b)

