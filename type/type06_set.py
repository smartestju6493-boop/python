# set = 순서 x, 중복 x(중복되도 그값 하나만)

a = {"1", "2", "4", "3", "3"}
print(a)

# 숫자는 정렬되더라...
# 숫자는 hashing 할 때 숫자 자체가 주소값으로 저장됨 숫자만 가능함 문자는 임의의 숫자나열로 바꿔버림
b = {1, 5, 4, 3, 2, 6}
print(b)
print([hash(x) for x in [1, 2, 3, 5, 4, 2]])

#set()
c = set ([1, 2, 3, 4, 5])
print(c)

c.add(6)
print(c)
print(c.pop())
print(c)

# set() 안에 iterable 한 객체를 넣으면...?
d = set("hello,world!")
print(d)
print([hash(x) for x in (d)])

# 똑같은 연산을 하고 있으면 위아래 결과가 동일(같은 메모리 공간에서)
left = {'a', 'b', 'c', 'd'}
right = {'c', 'd', 'e', 'f'}
print(left.union(right))
print(left | right)

#교집합
print(left.intersection(right))
print(left & right)

#차집합
print(left.difference(right))
print(left - right)

# frozenset 변경할수없다
e = frozenset({1, 2, 3, 4, 5})
print(e)
#e.pop()  불가능


#두개 차이
print(dir(set))
print(dir(frozenset))
