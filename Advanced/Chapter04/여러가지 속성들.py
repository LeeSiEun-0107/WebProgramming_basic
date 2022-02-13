class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체마다 다른 값을 가지는 속성

    클래스 속성 : 전체 유닛 개수
    -> 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성
    """
    count = 0

    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.__hp = hp
        self.damage = damage
        self.shield = shield
        Unit.count += 1  # 클래스 속성
        print(f"{self.name}이 생성되었습니다")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp}"


probe = Unit("프로브", 20, 20, 5)  # 프로브 만의 인스턴스 속성을 가짐
zealot = Unit("질럿", 100, 60, 16)
dragon = Unit("드라군", 100, 80, 20)

# class 밖에서 접근 할 때 : 인스턴스 속성 수정
probe.damage += 1

# 비공개 속성 접근 but 바뀌지 않음
probe.__hp = 9999

# 네임 맹글링 (name mangling)으로 비공개 속성 접근 가능
probe._Unit__hp = 9999

print(probe)
print(zealot)
print(dragon)

# 전체 유닛 개수
print(Unit.count)
