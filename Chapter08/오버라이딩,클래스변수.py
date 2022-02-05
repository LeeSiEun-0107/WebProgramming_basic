import random
# 클래스 변수 : 인서턴스 들이 모두 공유하는 변수


class Monster:
    max_num = 1000

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1  # 클래스 변수, 클래스 자체의 변수

    def move(self):
        print(f"{self.name} 움직임")


class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)  # 부모클래스의 init 함수를 불러와서 호출할 수 있음
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def skiil(self):
        print(f"{self.name} 스킬 사용 {self.skills[random.randint(0,2)]}")


dragon = Dragon("드래곤", 10, 20)
dragon.skiil()
print(dragon.max_num)
