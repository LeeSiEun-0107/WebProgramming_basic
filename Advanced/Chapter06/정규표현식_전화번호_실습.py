"""
Jason 팀장 : YYYY/MM/DD 형식으로 표현된 날짜를 검사
"""
# 연도는 4자리 숫자로 제한한다.
# 월은 1~12월, 일은 1~31일 까지 가능
import re

datas = ["2022/08/08",
         "1000/01/01",
         "9999/12/31",
         "900/02/02",
         "12000/10/26",
         "2021/13/01",
         "2023/2/02",
         "2024/06/3",
         "2023/06/35"]


for data in datas:
    match = re.match("^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[0-1])$", data)
    result = (lambda x: True if x != None else False)(match)
    print(f"{data} : {result}")
