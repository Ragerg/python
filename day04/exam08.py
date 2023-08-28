data = [10, 20, 30, 40]

print(data)
print(*data) # print(10, 20, 30, 40)

def getTotal(a, b, c, d):
    return a+b+c+d

def getSum(nums):
    s = 0
    for i in nums:
        s += i
    return s

def getSum(*nums):
    # print(nums, type(nums))
    s = 0
    for i in nums:
        s += i
    return s

print(f'총합 : {getTotal(1, 2, 3, 4)}')
print(f'총합 : {getTotal(10,20, 5, 6)}')
print(f'총합 : {getTotal(*data)}') # getTotal(10, 20, 30, 40)
print(f'총합 : {getTotal(*[10, 20, 30, 40])}')

# print(getSum([10, 20, 30, 40]))
print(getSum(10, 20, 30, 40))
print(getSum(10, 20, 30, 40, 50))
print(getSum(10, 20))