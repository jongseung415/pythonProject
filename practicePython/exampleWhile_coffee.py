coffee = 10
insertedCoin = 0

# coffee 원툴
while coffee != 0:
    print("커피를 드시려면 300원을 투입해주세요.")
    print("투입 대기:")
    insertedCoin = int(input())
    if insertedCoin == 300:
        print("커피 내리는 중...")
        coffee -= 1
    elif insertedCoin >= 300:
        print("커피 내리는 중...")
        coffee -= 1
        exchange = insertedCoin - 300
        print("잔돈은 %d원 입니다." % exchange)
    else:
        needMoreCoin = 300 - insertedCoin
        print("동전이 %d원 모자랍니다." % needMoreCoin)
        print("동전을 반홥합니다.")

    if coffee == 0:
        print("품절!")
        break