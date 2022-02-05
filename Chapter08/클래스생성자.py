from turtle import speed


class Monster:
    # init->인스턴스 만들때 가장 먼저 호출, self는 매게변수로 치지 않는다.
    def __init__(self, health, attack, speed):
        self.health = health  # 호출된 인스턴스의 health에다가 health인자를 저장해라
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):  # 체력 감소
        self.health -= num

    def get_health(self):  # 체력 가져오기
        return self.health


goblin = Monster(800, 120, 300)  # self=goblin
wolf = Monster(1500, 200, 300)  # self=wolf

goblin.decrease_health(100)
print(goblin.get_health())
