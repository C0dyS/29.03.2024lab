class Basket:
    def __init__(self):
        self._basket = {}

    def add_item(self,item,price):
        if item in self._basket:
            print("item already in the basket")
        else:
            self._basket[item] = price
    def check_basket(self):
        print(self._basket)

    def basket_price(self):
        return sum(self._basket.values())




check = Basket()
check.add_item('asf',13)
check.add_item('asfa',15)
check.add_item('asfa',15)
check.check_basket()
print(check.basket_price())