# f(x) = 함수 = 입력 -> 처리 -> 출력 : 기능

def hello01() :
    print("hello, world!")
    print('hello, python!')


hello01()
print(hello01())


def hello02() :
    msg = "hello, python!!!"
    return msg

print(hello02())

def hello03() :
    return {"name" : "admin", "massage" : "hello, service"}

print(hello03())

result = hello03()
print(f"name : {result["name"]}")
print(f"massage : {result["massage"]}")

def hello04() :
    print("no return")
    return
# 리턴 되는 닶이 없다 = none]
print(hello04())
hello04()

def hello05() :
    return 1
    return 2
    return 3

print(hello05())

#print(hello05) 함수라는 객체 위치를 알려줌
