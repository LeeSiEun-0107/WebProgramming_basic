class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    클래스 속성 : 전체 유닛 개수
    """
    count = 0

    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.shield = shield
        Unit.count += 1
        print(f"{self.name}이 생성되었습니다")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 데미지 : {self.damage} 쉴드 : {self.shield}"

    # 인스턴스 메서드 (instance method) : 메모리 상에 객체가 실체한다.
    # 인스턴스 속성에 접근할 수 있는 메서드

    def hit(self, damage):
        # 방어막 변경하는 로직
        if damage <= self.shield:
            self.shield -= damage
            damage = 0
        else:
            damage -= self.shield
            self.shield = 0

        if damage > 0:
            if self.hp > damage:
                self.hp -= damage
            else:
                self.hp = 0

    # 클래스 메서드 (class method)
    # 클래스 속성에 접근하는 메서드 , 데코레이터를 사용해 준다.
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 :[{cls.count}]개")


probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragon = Unit("드라군", 100, 80, 20)

print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)

Unit.print_count()

print(dir(probe))
