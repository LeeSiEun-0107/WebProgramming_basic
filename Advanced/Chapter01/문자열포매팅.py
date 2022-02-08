# 문자열 포매팅이 없다면?
# 시은님. 수강기간이 7일 남았습니다.

name = "시은"
duration = "7"

message = name + "님 수강기간이 " + duration + "일 남았습니다"
print(message)


# 문자열 포매팅으로 메세지 출력

name = "시은"
duration = "7"
print(f"{name}님 수강기간이 {duration}일 남았습니다")

# format 메서드 사용
print('안녕? {0} {1} {2}'.format("apple", "baby", "shutup"))
print('안녕? {1} {2} {0}'.format("apple", "baby", "shutup"))

# f-string 사용
name1 = "apple"
name2 = "pineapple"
name3 = "pen"

c = f"Hello {name1}, {name2}, {name3}"
print(c)
