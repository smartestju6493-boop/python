# 산술연산 int에서 dir을 해보면 확인할수있는 구조,기능에 아래 연산이 들어있다
a = 17
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 거듭제곱 (power)
print(a ** b)

# 몫 (floor division : 소수점 이하는 버림)
print(a // b)

#나머지 (modulo)
print(a % b)

#비교연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <=b)
# print(a =< b) 항상 등호가 뒤쪽에 온다
print(a is b)
print(a is not b)

# 여러개 한번에 비교도 가능 지원가능한 프로그램인지 확인필요
print(1 < b < a)
print(1 < a < b)

# and : 둘 다 참(true) 이여야지만 참(true)
print(True and False)
print(True & False)
# or : 둘 중 하나만 참(treu)이면 참(true)
print(True | False)
print(True or False)
# not : 참은 거짓으로 거짓은 참으로 바꿔줌 True -> False , False -> True
print(not True)
print(not False)

# 멤버연산
list01 = [1, 2, 3, 4, 5]

print(3 in list01)
print(6 in list01)
print(3 not in list01)

#range : 해당 범위의 숫자 생성 메모리 절약에 좋음 (시작값과 끝값만 저장함)
print(range(10))
#range(stop) : 0 ~ stop ? stop -1 까지 표현
print(list(range(10)))
#range(start, stop) : start ~ stop -1
list02 = list(range(10, 20))
print(list02)
#range(start, stop, step) : start, start + step, start + step + step, ...... , step-1
print(list(range(1, 11, 2)))
# 10 ~ 1 거꾸로
print(list(range(10, 0, -1)))
lista = list(range(1, 11))
lista.reverse()
print(lista)

# slice
original = list(range(100))
print(original)

# [n] : n index 위치를 0부터 표현 0번째부터 시작
print(original[5])
print(original[0])
# [start, stop] 위치부터 stop-1까지 표현 start index ~ stop index -1
slice01 = original[1 : 5]
print(slice01)
# [start, stop, step]
slice02 = original[10 : 20 : 2]
print(slice02)

# 숫자가 없으면?
print(original[: 50])
print(original[50 :])
print(original[:: 10])

#거꾸로
slice03 = original[20: 10: -1]
print(slice03)

hello = "hello, world!"
print(hello)

# !를 빼고 출력하고 싶어 단어순서를 index로 순서로 생각
print(hello[0: 12])
print(hello[: 12])
print(hello[: -1])

# -1
print(hello[-1])
print(hello[: -1])
print(hello[: : -1])

# world 만 출력하고 싶어
print(hello[7 :12])
print(hello[7 : 12 : 1])
# 증강 연산자
c = 10

# c라는 변수에 저장된 값에다가
# 1을 증가시켜서
# 다시 c에 저장하고 싶어... 신텍스 슈거
c = c + 1
print(c)
c += 1
print(c)

c -= 1
print(c)

c *= 2
print(c)

c /= 2
print(c)

c **= 2
print(c)
