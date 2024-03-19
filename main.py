class Eg:
    def __init__(self,amount):
        self._amount = amount

    def check_balance(self):
        return self._amount

    def deposit(self,new_amount):
        self._amount += new_amount

    def withdraw(self,withdraw_amount):
        if self._amount >= withdraw_amount:
            self._amount -= withdraw_amount
        else:
            print('not enough $$$')


test = Eg(100)
print(test.check_balance())
test.deposit(40)
print(test.check_balance())
test.withdraw(20)
print(test.check_balance())
test.withdraw(4000)
