# 기존 함수
def minus(a):
    return -a


# 람다 함수
lambda a: -a

# 람다 함수 호출 방법 1. 함수 자체를 호출
print((lambda a: -a)(10))

# 람다 함수 호출 방법 2. 변수에 담아서 호출


def minus_anwer(a): return -a


print(minus_anwer(10))

# 기존 함수


def positive_number(a):
    if a > 0:
        return True
    else:
        return False


# 람다 함수
print((lambda a: True if a > 0 else False)(-3))
