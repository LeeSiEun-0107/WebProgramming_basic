import pay_module
# 변수 사용
print(pay_module.version)
pay_module.printAuthor()
# 클래스 사용
pay_info = pay_module.Pay("A1234", 13000, "2021-06-13")
print(pay_info.get_pay_info())
