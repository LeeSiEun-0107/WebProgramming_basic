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
    p.join()  # main이 sub가 종료될때 까지 기다려줌
    print("main end")

# 뭔소린지 모르겠다..ㅎ
