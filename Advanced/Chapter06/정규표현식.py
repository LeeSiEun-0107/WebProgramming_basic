import re

# 1. re 모듈의 메서드
str = 'love people around you, love your work, love yourself'

# 1) match : 문자열의 처음부터 검색해서 결과로는 1개의 match 객체가 나옴
result = re.match('love', str)
print(result)

# 2) search : 문자열의 전체를 검색해서 1개의 match 객체가 나옴
result = re.search('people', str)
print(result)

# 3) findall : 문자열의 전체를 검색해 모든 문자열 리스트가 나옴
results = re.findall("love", str)
print(results)

# 4) finditer : 문자열의 전체를 검색해 match 객체 iterator가 나옴
results = re.finditer("love", str)
print(results)

for result in results:
    print(result)

# 5) fullmatch : 패턴과 문자열이 오나벽하게 일치하는지 검사
str2 = "Hey huys, read books"
result = re.fullmatch(".*", str2)
print(result)

# 2. match 오브젝트 메서드
result = re.search('people', str)

# 1) group():매칭된 문자열을 반환해줌
print(result.group())

# 2) start():매칭된 문자열의 시작을 반환해줌
print(result.start())

# 3) end() : 매칭된 문자열의 끝을 반환해줌
print(result.end())

# 4) span() : 매칭된 문자열의 (시작,끝) 튜플을 반환해줌
print(result.span())
