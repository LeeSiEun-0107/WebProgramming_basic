# 1. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)


print_fruits('apple', 'orange', 'mango', 'grapes')

# 2.키워드 가변 매개변수


def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


comment_info(name="파린이", content="정말갑사합니다")

# 매개변수를 작성하는 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변


def post_info(title, content, *tags):
    print(title, content, tags)
