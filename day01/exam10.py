# data = input('데이터를 입력하세요').split()
# print(data)

num = 29
i = 2
while i < num and num % i :
    i += 1
print('소수' if i == num else '비소수')