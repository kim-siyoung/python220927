# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기화 메서드
    def __init__(self, id, name, balance):
        # self.id = id
        # self.name = name 
        # self.balance = balance 
        # 이름 변경(이름 규칙)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    # 입금
    def deposit(self, amount):
        # self.balance += amount 
        self.__balance += amount 
    # 출금
    def withdraw(self, amount):
        # self.balance -= amount
        self.__balance -= amount
    # 결과 문자열
    def __str__(self):
        # return "{0} , {1} , {2}".format(self.id, \
        #     self.name, self.balance)
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)
# print(account1.__balance) # 밖에서는 __balance로 접근 안됨 
# 외부에서는 _클래스명_변수명 => 백도어(테스트 용도) ... 자동완성 안되면 가능한 쓰면 안좋음
print(account1._BankAccount__balance)
#account1.balance=15000000
#print(account1.balance) 쓰기 읽기 다 가능하면 문제있음 변수를 숨겨야함(클래스 안에)
