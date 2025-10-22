# 전역변수 (파일 전체에서 사용가능하다)
x = 10


def test01() :
    print(x)

def test02() :
    # 지역변수 해당 지역 안에서만 사용가능
    x = 20
    print(x)


def test03() :
    # 전역변수 x를 사용하고 싶어 전역변수를 바꿈
    global x
    x = 30
    print(x)


test01()
test02()
test03()

print(x)


print("-----")

def test04() :
    global y   #-> 전역변수화
    y = 3
    print(y)

test04()

print(y)


# shadowing : 3개의 y는 모두 다른 y

def outer01() :
    y = 6

    def inner01() :
        y = 9
        print(f"inner y : {y}")

    inner01()
    print(f"outer y : {y}")

outer01()
print(f"global y : {y}")

print("-----")


def outer02() :
    global y
    y = 6

    def inner02() :
        y = 9
        print(f"inner y : {y}")

    inner02()
    print(f"outer y : {y}")


outer02()
print(f"global y : {y}")

print("-----")


def outer03() :
    y = 9

    def inner03() :
        nonlocal y    # 지역 변수로 사용하는게 아니다 덮고 있는 바로 위에있는 변수를 대체하겟다.
        y = 3
        print(f"inner y : {y}")

        def inner_inner01() :
            nonlocal y
            y = 1
            print (f"inner_inner01 y : {y}")

        inner_inner01()

    inner03()
    print(f"outer y : {y}")


# python namespace

outer03()
print(f"global y : {y}")
