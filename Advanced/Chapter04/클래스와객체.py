# Unit 클래스
class Unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    """

    # 생성자
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, shield, damage):  # self는 객체 자기자신을 의미함!
        # 객체의 속성을 초기화 시켜줌
        self.name = name
        self.hp = hp
        self.damage = damage
        self.shield = shield
        print(f"{self.name}이 생성되었습니다")

    # 객체를 출력할 때 호출되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp}"


# 프로브 객체 생성
probe = Unit("프로브", 20, 20, 5)

# 질럿 객체를 생성
zealot = Unit("질럿", 100, 60, 16)

# 드라곤 객체 생성
dragon = Unit("드라군", 100, 80, 20)

# 객체의 속성 정보를 출력
print(probe)
print(zealot)
print(dragon)
