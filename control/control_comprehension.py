list01 = list()
for i in range(1, 11) :
    list01.append(f"a{i}")

print(list01)

list02 = [f"a{i}" for i in range(1, 11)]
print(list02)

# 1 ~ 10 사이의 짝수만 list
list03 = [i for i in range(1, 11) if i % 2 == 0]
print(list03)

subjects = [
    "python", "analysis", "database",
    "html", "css", "javascript", "django",
    "science", "engineering"]
# subjects 안의 item 들 중에, a 를 포함하고 있는 item들만 새로운 list 로 만들자
list04 = [sub for sub in subjects if "a" in sub]
print(list04)

# 중첩
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# [4*n 4*n+1
list05 = [[4 * i + j for j in range(4) ] for i in range(4)]
print(list05)

