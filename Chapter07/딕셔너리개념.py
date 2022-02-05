stock_a = {"삼성전자": 82000, "LG전자": 150000}
stock_b = {
    "삼성전자": [82000, 1, 2, 3, 4],
    "LG전자": [150000, 1, 2, 3, 4]
}
stock_c = {
    "삼성전자": {
        "현재가": 82000,
        "보유수량": 5,
        "매수단가": 81000
    }
}

print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])
print(stock_c["삼성전자"].items())


# items() : 키와 데이터 쌍
for item in stock_c["삼성전자"].items():
    key, value = item
    print(key, value)

# keys() : 키
for key in stock_b.keys():
    print(key)

# values() : 데이터
for value in stock_b.values():
    print(value)
