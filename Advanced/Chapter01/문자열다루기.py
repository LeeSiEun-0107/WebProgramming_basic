# 1. replace
# 문자열 교체 메서드
print("오늘 날씨는 흐림 입니다".replace("흐림", "맑음"))

# 2. find
# 문자열 찾고 index 반환, 없을 시 -1반환
print("Hello world".find("world"))

# 3. split
# 문자열을 분리하는 메서드
print("나이키 265 X122 7000".split())

# 4. strip
# 문자열 공백 제거
print("     yeah     ".lstrip())  # 왼쪽 공백 없어짐
print("     yeah     ".rstrip())  # 오른쪽 공백 없어짐
print("     yeah     ".strip())  # 양쪽 공백 없어짐
