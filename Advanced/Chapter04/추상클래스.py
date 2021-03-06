from abc import *


class Item(metaclass=ABCMeta):
    """
    속성 : 이름
    메서드 : 줍기, 버리기
    """

    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"{self.name}을 주웠다!")

    def discard(self):
        print(f"{self.name}을 버렸다..")

    @abstractmethod
    def use(self):
        pass


class Weapon(Item):
    """
    속성 : 공격력
    메서드 : 공격하기
    """

    def __init__(self, name, damage):
        super().__init__(name)  # 부모 클래스를 호출하는 역할
        self.damage = damage

    def use(self):
        print(f"{self.name}을 이용해서 {self.damage}로 공격합니다!")


class HealingItem(Item):
    """
    속성 : 회복력
    메서드 : 사용하기
    """

    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"{self.name}을 사용합니다. {self.recovery_amount} 회복")


m16 = Weapon("M16", 110)
bungdae = HealingItem("붕대", 20)

m16.use()
bungdae.use()
