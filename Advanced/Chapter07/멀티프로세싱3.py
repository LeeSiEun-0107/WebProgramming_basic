from multiprocessing import Process
import time


class Subprocess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"sub {self.name} start")
        time.sleep(3)
        print(f"sub {self.name} end")


if __name__ == "__main__":
    print("main start")
    p = Subprocess(name="startcoding")
    p.start()
    time.sleep(1)
    # 프로세스가 살아있는지 검사
    if p.is_alive:
        p.terminate()

    print(p.is_alive())  # 서브 프로세스가 살아있다는 의미
    print("main end")

# 뭔소린지 모르겠다..ㅎ

# 공부 할 만한 내용
# 1. 스레드간 데이터 처리 => lock 공부
# 2. 프로세스 간 데이터 전송 방법 (Queue,pipe)
# 3. 속도 비교하는 예제 만들어 보기
# 4. 운영체제와 메모리
