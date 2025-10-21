# tuple : list 와 거의 같음 (변경이 불가능)

#( 값, 값, 값, ... )
a = (1, 2, 3, 4, 3)
print(a)
print(type(a))

#생성자
b = tuple([5, 6, 7, 8])
print(b)
print(type(b))

# a.append(6)
# a.pop()
print(dir(a))

print(a.count(6))

# tuple + tuple
c = a + b
print(c)
print(type(c))

#형 변환
# tuple -> list
d = list(c)
print(d)
print(type(d))
d.remove(7)
print(d)

# list -> tuple
e = tuple(d)
print(e)
print(type(e))


# packing
f = 1, 2, 3
print(f)
print(type(f))

#unpacking
g, h, i = f
print(g)
print(h)
print(i)

"""
j, k = f
print(j)
print(k)
"""


