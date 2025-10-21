# 여러 개의 값을 효과적으로 관리하기 위한 객체들
# -> list, tuple, set, dictionary

# Sequence : 순서가 있는 갋들을 가진 객체

# list : 순서 o, 중복 o

# [ 값, 값, 값 ]
a = [5, 3, 4, 2, 3, 1,3]
print(a)
print(type(a))

a.append(6)
print(a)

# list() 생성자
b = list()
print(type(b))
b.append(7)
b.append(9)
b.append(8)
b.append(9)
print(b)

# list 에서 특정 값 가져오기
# list(index)
# index 는 보통 0부터 시작!
# a = [5, 3, 4, 2, 3, 1, 3, 6]
print(a[2])
# b = [7, 9, 8, 9]
# 첫번째 9를 가져오고 싶어
print(b[1])

# dir : 객체의 속성, 매서드를 확인
print(dir(list))
# __??__ : special method (magic mathod)
# __iter__ : 반복가능한 (iterable) => iterator
# __len__, __getitem__ : 연속적인 (sequenceable)

# list 를 거꾸로 출력
b.reverse()
print(b)

# list 의 값을 뺴내오고 싶어
# 맨 뒤에서 하나 빼와
print(a)
print(a.pop())
print(a)

# lsit 정렬하고 싶어
print(a.sort())
print(a)

# lsit 의 크기 알려줘
print(len(a))

# list 연산
# list + list
c = a + b
print(c)
print(type(c))

# * : 곱하기
print(a*2)

# index 3 위치에 숫자 999를 넣어보자
c.insert(3, 999)
print(c)

# 중첩
d = ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h'], 'i']
print(d)
print(len(d))

# g 출력하고 싶어
print(d)
print(d[5][1])

#






