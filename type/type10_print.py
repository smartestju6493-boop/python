# print
# flush : stream에 남아있는 데이터를 강제로 출력

name = "ju"
age = 100

# name 과 age 를 출력하자
# print(name + age) str은 str 끼리만 더할수있다.
print(name + str(age))
print(name, age)

# *args / **kwargs 중요! (str, age)이 되는 이유는 얘네 덕분이다

print(name, age, sep="-")

print(name, age, end="출력이 끝난 후 end가 출력됩니다...")
print("??")

print("name", name, sep=":", end="\t")
print("age", age, sep=":")

# % values
print("name: %s" % name)
print("name: %s \t age: %d" % (name, age))

# str.format()
print("name: {} \t age: {}".format(name, age))

# f-string
print(f"name: {name} \t age: {age}")


