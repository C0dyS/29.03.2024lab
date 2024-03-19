class User:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_email(self):
        return self._email
    def set_age(self,new_age):
        self._age = new_age


alex = User('alex',15,'asd')
print(alex.get_age())
alex.set_age(21)
print(alex.get_age())