# int : 정수
a = 100
print(a)

# int 생성자 -> 객체 생성
b = int(101)
print(b)

# float : 실수
c = 200.2
print(c)

d = float(200.3)
print(d)

# int + float = float
print(a + d)
print(type(a + d))

# complex : 복소수
# real + imaginary (실수부 + 허수부j)
e = 1 + 2j
print(e)
print(type(e))

# complex(real, imgae)
f = complex(3,4)
print(f)

# bool : 논리
g = True
h = False
print(g)
print(h)

print(type(g))

# c 언어 -> true : 1 / flase : 0 => python에서도 동일
print( 1 == g)
print(0 != g)

# 진수 변경
# 2진수 (0b)
binary = 0b1111
print(binary)
#8진수 (0o)
octal = 0o77
print(octal)
#16진수 = (0x)
hexadecimal = 0xff
print(hexadecimal)


