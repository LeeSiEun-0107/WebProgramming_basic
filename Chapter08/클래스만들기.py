class Monster:
    def say(self):
        print("나는 몬스터다")


goblin = Monster()  # goblin이라는 인스턴스 변수에 담아준다
goblin.say()  # 메서드 호출

# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열"
c = True
print(type(a), type(b), type(c))

print(b.__dir__()) #클래스 메서드 확인 방법
