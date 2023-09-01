try:
    num = int(input('짝수를 입력하세요 : '))
    if num % 2:
        raise Exception(f'입력하신 정수 {num}은 짝수가 아닙니다') # 강제 예외
except Exception as e:
    print(e)