# while 조건:
# 조건이 참(true)인 동안 반복한다.

i = 1

while i <= 10 :
    print(i)
    i += 1

my_sum = 0
my_count = 1

#반복이 끝날때 else 구문을 표현하라
while my_count <= 10 :
    my_sum += my_count
    my_count += 1
else :
    print(f"sum : {my_sum} \t count : {my_count}")