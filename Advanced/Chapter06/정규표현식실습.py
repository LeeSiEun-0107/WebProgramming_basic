import re

# 전화번호 정규 표현식 연습
# https://regexr.com/63bls

# 1. Group 그룹

# 1) 매칭되는 문자열 한개
str1 = '010-2343-3333'
result = re.match('\d{2,3}-\d{3,4}-(\d{4})$', str1)  # $:문장의 끝
print(result.group(1))  # 1 번째 그룹 출력, () : 그룹

# 2) 매칭되는 문자열 여러개
str2 = '010-2343-7888,010-2343-1234,010-2343-5678,010-2343-9999,010-2343-2222'
results = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=,|$)', str2)

for idx, result in enumerate(results, 1):
    print(f"{idx}. {result.group(1)}")

# 2. substitution (교체)
str3 = '010-2343-3333'
result = re.sub('(?<=\d{3}-\d{4}-)\d{4}', '****', str3)
print(result)
