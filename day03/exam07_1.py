num, num2 = map(int, input('정수 2개 입력하세요 : ').split())
print(num, num2)

divNum = [i for i in range(1, num+1) if num % i == 0]
divNum2 = [i for i in range(1, num2+1) if num2 % i == 0]
divisor = [n for n in divNum if n in divNum2]

print(divNum)
print(divNum2)
print(f'{num}, {num2}의 최대 공약수 : {max(divisor)}')
print(f'{num}, {num2}의 최대 공약수 : {max(set(divNum) & set(divNum2))}')