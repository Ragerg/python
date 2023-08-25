# 정수 2개 입력받아 최대공약수 출력

num1, num2 = input('정수 2개 입력하세요 : ').split()

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp

while(num2):
    a = int(num1) % int(num2)
    num1 = num2
    num2 = a

print(f'최대공약수 : {num1}')
