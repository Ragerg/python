'''
num01 = input('첫 번째 정수 입력 : ')
num02 = input('두 번째 정수 입력 : ')
print(num01, num02)
'''

# print(type('12, 5'.split())) ## <class 'list'>
num01, num02 = map(int, input('두 개의 정수를 입력 : ').split())
print(type(num01), type(num02))
