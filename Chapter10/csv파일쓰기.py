import csv

data = [
    ["이름", "반", "번호"],
    ["제석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 3, 2]
]

file = open("./myvenv/Chapter10/student.csv",
            "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()
