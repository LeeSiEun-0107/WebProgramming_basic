# 생성자 : 인스턴스를 만들 때 호출되는 메서드
# 객체가 인스턴스를 포함하는 개념이고 인스턴스는
# 프로그램이 동작할 때 객체가 만들어진 시점의 객체

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health


# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(10, 10, 10)
wolf.decrease_health(20)
print(wolf.get_health())
