korea = int(input("국어"))
math = int(input("수학"))
english = int(input("영어"))

if korea < 0 or korea > 100 or korea < 0 or math > 100 or english < 0 or english > 100:
    print("잘못 입력 하셨습니다")
elif (korea+english+math)//3 >= 80:
    print("불합격")
else:
    print("합격")
