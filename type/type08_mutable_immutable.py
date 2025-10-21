# mutable : list, set, dictionary 값이 변화가능
a = [1, 2, 3, 4, 5]
print(a)
print(id(a))

a.append(6)
print(a)
print(id(a))

z = [1, 2, 3, 4, 5, 6, 7]
print(z)
print(id(z[0]))

q = [ 11, 12, 13, 14, 15, 16, 17 ]
print(q)
print(id(q))


# immutable : neumbers, tuple, str, frozenset  값이 변화 불가능
b = 10
print(b)
print(id(b))

b = 20
print(b)
print(id(b))

c = (1, 2, 3, 4, 5)
print(c)
print(id(c))

c = c + tuple(a)
print(c)
print(id(c))