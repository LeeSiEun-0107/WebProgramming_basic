# 1.map함수
# 기존 리스트를 수정해서 새로운 리스트를 만들 때 사용
# map(함수,순서가 있는 자료형)

list(map(int, ['3', '4', '5', '6']))

# 리스트 모든 요소의 공백 제거하는 예제
items = ['   옷    ', '     키보드     ']

# for i in range(len(items)):
#     items[i] = items[i].strip()
# print(items)

# 람다 함수 사용
print(list(map(lambda x: x.strip(), items)))

# 2.filter 함수
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 경우 사용
# filter(함수,순서가 있는 자료형)


def func(x):
    return x < 0


print(list(filter(func, [-3, -2, 0, 7])))

animals = ['cat', 'tiger', 'rabbit']

print(list(filter(lambda animal: len(animal) >= 4, animals)))
