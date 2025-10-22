# type annotation type
# type hint

# 함수의 return 값이 있는 경우 , 해당 값의 type 을 설명 화살표 뒤에 : 뒤에 타입을 써주면 결과의 일반적인
def test01(a, b) -> int :
    x, y = int(a), int(b)

    return x + y


# parameter 의 타입 설명
def test02(a : int, b : str) -> str :
    result = str(a) + b

    return result

# parameter : type = default 값을 주지 않으면 주어진값으로
def test03(a : int=0, b : int=0) -> int :
    return a + b

if __name__ == "__main__":
    # 변수 type 명사
    c : int = 1
    print(test01(c, 2))

    print(test02(1, "2"))

    print(test03(1))

    # pep484