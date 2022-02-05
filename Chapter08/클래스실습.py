# item 종류 구분한다면

import random


class MMORPG:
    my_weight = 100

    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropalbe = isdropable

    def sale(self):
        self.price -= 50
        print(f"{self.name}을 판매하셨습니다")

    def discard(self):
        self.isdropalbe = False
        MMORPG.my_weight -= self.weight
        print(f"아이템을 버리셨습니다. 제 몸무게는 {MMORPG.my_weight}kg 입니다")


class WearableItem(MMORPG):
    def __init__(self, name, price, weight, isdropable):
        super().__init__(name, price, weight, isdropable)
        self.effect = ["샤방샤방", "잘생김", "이건 좀..."]

    def wear(self):
        MMORPG.my_weight += self.weight
        return print(f"{self.name}을 입었습니다. 저의 몸무게는 {MMORPG.my_weight}입니다. 입은 효과는 {self.effect[random.randint(0,2)]} 이네요")


class UsableItem(MMORPG):
    def __init__(self, name, price, weight, isdropable):
        super().__init__(name, price, weight, isdropable)
        self.effect = ["때려부수기", "죽이기", "뺨때리기", "발로차기"]

    def use(self):
        self.weight_ = 500
        return print(f"{self.name}을 사용했습니다. 저의 몸무게는 {self.weight}입니다. 사용 효과는 {self.effect[random.randint(0,2)]} 이네요")


sieun = WearableItem("마법망토", 30, 10, True)
sieun.sale()
sieun.wear()
sieun.discard()

sora = UsableItem("몽둥이", 2000, 300, True)
sora.use()
