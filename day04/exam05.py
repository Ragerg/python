# quit 가 나올 때까지 문자열을 입력받아 test02.txt 저장
# test02.txt 에 저장된 모든 문자열 읽어서 모니터에 출력

# with open('test02.txt', 'w') as file:
#     print('문자열들을 입력하세요. quit 입력 시 종료')
#     while True:
#         msg = input()
#         if msg == 'quit':
#             break
#         # file.write('{0}\n.format(msg))
#         file.write(f'{msg}\n')
#
# print('파일 저장 완료....')

print('<읽어 온 데이터>')
with open('test02.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip('\n'))
