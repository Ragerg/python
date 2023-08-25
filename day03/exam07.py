# 정수 2개 입력받아 최대공약수 출력

num1, num2 = input('정수 2개 입력하세요 : ').split()

if num1 < num2:
    num1, num2 = num2, num1

while(num2):
    num1, num2 = num2, int(num1) % int(num2)

print(f'최대공약수 : {num1}')
