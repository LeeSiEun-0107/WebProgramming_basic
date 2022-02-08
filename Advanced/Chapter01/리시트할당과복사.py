import copy
x = [1, 2, 3, 4, 5]
y = x
y[2] = 0

print(x, y)
print(id(x), id(y))

a = [1, 2, 3, 4, 5]
b = a.copy()
b[1] = 20000
print(a, b)

# 중첩 리스트 복사 형식
c = [[1, 2], [3, 4, 5]]
d = copy.deepcopy(c)
d[0][0] = 1000000
print(c, d)
