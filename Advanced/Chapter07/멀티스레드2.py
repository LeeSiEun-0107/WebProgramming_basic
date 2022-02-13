from concurrent.futures import thread
import threading
import time

# 주식 자동 매매
# 매수, 매도를 한개의 프로그램에서 실행

# 매수 스레드


def buyer():
    for i in range(5):
        print("[매수] 데이터 요청중 ...")
        time.sleep(1)
        print("[매수] 데이터 분석중 ...")
        time.sleep(1)
        print("[매수] 지금 매수 타이밍이닷 ...")
        time.sleep(1)
        print("[매수] 풀매수함")
        time.sleep(1)


def seller():
    for i in range(5):
        print("[매도] 데이터 요청중 ...")
        time.sleep(1)
        print("[매도] 데이터 분석중 ...")
        time.sleep(1)
        print("[매도] 지금 매도 타이밍인갓?")
        time.sleep(1)
        print("[매도] 눈물머금고 손절")
        time.sleep(1)


print("메인이 스타트 되었당!")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)

buyer.start()
seller.start()

buyer.join()  # 매수 스레드가 종료될 때 까지 메인 스레드가 기다림
seller.join()  # 매도 스레드가 종료될 때 까지 메인 스레드가 기다림

print("메인이 끝났당!")
