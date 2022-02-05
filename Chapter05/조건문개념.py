input_pass = input("비밀번호를 입력하시오")
origin_pass = "1234"

if input_pass == "":
    print("비밀번호를 입력해주세요")
elif input_pass == origin_pass:
    print("비밀번호가 맞았습니다")
else:
    print("비밀번호가 틀렸습니다")
