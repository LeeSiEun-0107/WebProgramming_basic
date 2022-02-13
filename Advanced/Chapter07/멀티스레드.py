import threading

# 스레드에서 실행할 함수


def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하시오")
    print(f"[sub] {keyword}로 검색 시작 합니다")
    print("[sub] end")


# 메인 스레드 실행되는 부분
print("[main] start")
worker = threading.Thread(target=work)
worker.daemon = True  # 서브 스레드도 같이 종료
worker.start()

print("[main]는 자기 할일을 합니다")
print("[main] end")
