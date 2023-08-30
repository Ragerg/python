class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr # 외부에서 직접적인 접근을 할 수 없다. 비공개
    def getAddr(self):
        return self.__addr
    def setAddr(self, addr):
        self.__addr = addr
    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr: {self.__addr}')

p = Person('홍길동', 25, '서울')
p.info()
print(p.name)
print(p.age)
# print(p.addr)
# print(p.__addr) # error
print(p.getAddr())