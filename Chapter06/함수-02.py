import random


def getRandomNumber():
    while True:
        number = random.randint(1, 45)
        if number not in temp:
            temp.append(number)
            return number
        else:
            continue


temp = []

for i in range(6):
    getRandomNumber()

print(temp)
