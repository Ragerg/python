'''
    정수 2개 입력받아 사칙연산의 결과 출력
'''

print('첫 번째 정수를 입력 : ', end='')
num01 = int(input())
# print(type(num01))
print('두 번째 정수를 입력 : ', end='')
num02 = int(input())

print(num01, '+', num02, '=', num01 + num02)
print('%d - %d = %d' % (num01, num02, num01 - num02))
print('%d * %d = %d' % (num01, num02, num01 * num02))
print('%d / %d = %d' % (num01, num02, num01 / num02))
print('%d / %d = %f' % (num01, num02, num01 / num02)) # %f 는 기본 소숫점 6자리까지
print('{0} / {1} = {2}' .format(num01, num02, num01 / num02)) # 문자열과 관련된 포맷함수
print(f'{num01} / {num02} = {num01 / num02}')
print(f'{num01} / {num02} = {num01 // num02}') # 몫만 구하는 경우 // 사용
print(f'{num01} % {num02} = {num01 % num02}')
print(f'{num01} ** {num02} = {num01 ** num02}') # 거듭제곱
