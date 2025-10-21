#제어문

# if 조건 : 전제가 참이라면 아래를 표현해달라
a = 1

if a == 1 :
    print(f"{a} 는 1 입니다.")

# if ~ else 아니라면
b = 1
if a == b :
    print(f"{a} == {b}")
else :
    print(f"{a} != {b}")

# if ~ elif 조건추가
if a > b :
    print(f"{a} > {b}")
elif a < b :
    print(f"{a} < {b}")
else :
    print(f"{a} == {b}")


wheels = 3
engine = True

if engine :
    if wheels == 2 :
        print("오토바이")
    elif wheels == 4 :
        print("자동차")
else :
    if wheels == 3 :
        print("자전거")
