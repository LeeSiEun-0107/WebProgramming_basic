word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
answer = [i for i in word_list if i[0] == 'a']
print(answer)

word_list = ['오메가3', None, '비타민c500', None, '홍삼절편']
# if문과 else문 함께 있으면 앞에 쓴다.
answer = [i if i != None else '' for i in word_list]
print(answer)
