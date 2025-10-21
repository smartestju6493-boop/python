# str : text sequence

#single * 1
a = 'hello, world'
print(a)
print(type(a))

# escape sequence
b = 'hello, \'python\''

# single * 3 여러줄은 싱글이 3개
c = '''hello
python
    abc
        def'''
print(c)

# double * 1
e = "hello, world"
print(e)

#doule * 3
f = """hello
python
   abc
       def
       """
print(f)

# 혼합
g = "hello, 'python'"
print(g)
h = 'hello "python"'
print(h)

# str()
i = str("hello, world")
print(i)

# escape sequence
print("hello, \nworld")

# raw string (소대문자 r쓸떄)
j = "c:\test"
print(j)
k = r"c:\test"
print(k)

# str + str
print("hello" + " " + "world" + "!!")
# print("hello" - "o")-허용 안함
print("hello" * 2)

#print("hello" + 1)
print("hello" + str(1))
