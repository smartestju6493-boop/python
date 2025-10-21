# 비어있는 문자열 : false
if "" :
    print("false")
else :
    print("true")

# [], {}, () : false
if [] :
    print("false")
elif {} :
    print("false")
elif () :
    print("false")
elif [1] :
    print("true")

# 0 : false / 1 : true
if 0 :
    print("false")
elif 1 :
    print("true")

# None : false
if None :
    print("false")
else :
    print("true")

# 비어있는 객체를 이용할때를 대비해 기억합시다
