def greetings(name) :
    prefix = "안녕하세요! "

    #lexical scope : suffix 라는 함수가 선언 될 때, 함수의 범위(scope)가 정해짐
    # suffix 가 return 되면 greetings도 종료되지만, suffix를 실행 시 greetings의 환경(prefix, name)을 기억했다가 사용함
    def suffix() :
        return prefix + name + "님!! 환영합니다!!!"
    # *함수가 값으로 사용됨!* (일급 객체. 일급 함수, 일급 시민...)
    return suffix


if __name__ == "__main__":
    message = greetings("이주형")()
    print(message)