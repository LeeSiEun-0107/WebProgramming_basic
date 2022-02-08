import csv
# # 1.파일 만들기
# file = open("./myvenv/Chapter10/mystock.csv",
#             "w", newline="", encoding="utf-8-sig")
# writefile = csv.writer(file)

# # 2. 데이터 쓰기
# stocks = [
#     ["종목", "매입가", "수량", "목표가"],
#     ["삼성전자", "85000", "10", "90000"],
#     ["Naver", "380000", "5", "400000"]
# ]

# for stock in stocks:
#     writefile.writerow(stock)

# file.close()

file = open("./myvenv/Chapter10/mystock.csv",
            "r", newline="", encoding="utf-8-sig")
readfile = list(csv.reader(file))


def show_profilt(data):
    name = data[0]
    purchase_price = int(data[1])
    amount = int(data[2])
    target_price = int(data[3])

    profit = (target_price - purchase_price) * amount
    profit_ratio = (target_price / purchase_price - 1) * 100
    print(f"{name} {profit} {profit_ratio:.2f}%")


for i in readfile[1:]:
    show_profilt(i)
