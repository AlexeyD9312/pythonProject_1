from itertools import product


class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return (f"Назва : {self.name} \n "
                f"Вартість: {self.price} grn \n"
                f" Опис: {self.description} \n "
                f"Габарити: {self.dimensions} см ")


item_1 = Item("car", 100000, "very fast", (4200, 1800 , 1200))
item_2 = Item("Laptop", 8000, "Acer aspire",(37, 26, 3))
print(item_1.__str__())
print(item_2.__str__())


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return (f"Ім'я : {self.name} \n "
                f"Фамілія: {self.surname}  \n"
                f" Номер телефону : {self.numberphone} \n ")


uzer = User("Donald", "Trump", "+380666363157")
print(uzer.__str__())


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
       cart = f" Purchase {self.user} \n "
       for product, cnt in self.products.items():
           cart += f"{product.name} (x{cnt}) - {product.price} UAH \n"
           cart += f"Total: {self.get_total()} UAH"
           return cart


    def get_total(self):
        self.total = sum(item.price * cnt for item, cnt in self.products.items())
        return self.total


order1=Purchase(uzer)
order1.add_item(item_1, 1)
order1.add_item(item_2, 2)

print(order1)

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40


