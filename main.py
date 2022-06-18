class Item:
    pay_rate = 0.8  # The pay rate with 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to receive arguments
        assert price >= 0, f'Price {price} should be greater than 0'
        assert quantity >= 0, f'Quantity {quantity} should be greater than 0'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # pay_scale is class attribute


item1 = Item("phone", 100, 5)
# print(item1.calculate_total_price())
item1.apply_discount()
# print(item1.price)

item2 = Item("Laptop", 1000, 3)
# print(item1.calculate_total_price())
item2.pay_rate = 0.7
item2.apply_discount()
# print(item2.price)

# Access class attribute & instance attribute using magic method __dict__
print("Access class attribute", Item.__dict__)
print("Access instance attribute", item1.__dict__)

