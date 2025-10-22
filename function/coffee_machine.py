def coffee(quantity, price, u) :
    change = price - (((quantity-u) * 200) + (u * 500))
    if change >= 0 :
        prn(quantity, change)
    else :
        prn()


def prn(quantity=0, change=0) :
    if quantity == 0 & change == 0 :
        print("금액이 부족합니다.")
    else :
        print(f"커피 {quantity}잔과 잔돈 {change}원이 나왔습니다.")


def start() :
    q = int(input("커피 몇 잔이 필요하신가요??"))
    u = int(input("고급 커피는 몇 잔 필요하신가요?"))
    p = int(input("금액을 넣어주세요 (1잔에 200원, 고급은 한잔에 500원)"))

    coffee(q, p, u)
