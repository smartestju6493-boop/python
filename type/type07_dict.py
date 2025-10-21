# dictionary
# 순서 o, 중복 (key x, value o)
# python 3.6 부터 순서가 가능해졌음

# {key: value, ...}
dict01 = {'a' : 1, 'b' : 2}
print(dict01)
print(type(dict01))

dict01['c'] = 3
print(dict01)
print(dict01['b'])

#제이슨 파일과 유형 크롤링할때 많이 쓰니 주의 ~12

# dict()
dict02 = dict(a=1, b=2)
print(dict02)

dict03 = dict([['a',1], ['b', 2]])
print(dict03)

print(dir(dict))

print(dict03.keys())
print(dict03.values())
print(dict03.items())

dict04 = dict([ ('a', 1), ('b', 2) ])
print(dict04)

print(list(dict04.keys()))