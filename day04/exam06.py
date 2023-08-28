print('<읽어 온 데이터>')
with open('test02.txt', 'r') as file:
    for line in file:
        print(line.rstrip('\n'))

# 방법 2
# with open('test02.txt', 'r') as file:
#     line = file.readline().rstrip(('\n'))
#     while line != '':
#         print(line)
#         line = file.readline().rstrip(('\n'))

# 방법 1
# with open('test02.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if line =='':
#             break
#         print('[{}]'.format(line.rstrip("\n")))
