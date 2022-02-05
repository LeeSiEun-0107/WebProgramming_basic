# 상속
#: 클래스들에 중복된 코드를 제거하고 유지, 보수를 편하게 하기 위해서 사용한다.

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"{self.name} 지상에서 이동하기 ")

# 자식 클래스 정의


class Wolf(Monster):  # (상속받은 클래스)
    pass  # 몸체를 만들고 싶지 않을 때 사용


class Shark(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")


class Dragon(Monster):
    def move(self):
        print(f"{self.name} 날기")


wolf = Wolf("울프", 1400, 200)
wolf.move()  # Monster의 메서드 사용
shark = Shark("샤크", 100, 200)
shark.move()  # Monster의 init 메서드 사용, 메서드 오버라이딩으로 재정의된 shark의 메서드를 사용
dragon = Dragon("드래곤", 8000, 800)
dragon.move()
