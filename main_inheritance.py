import csv


class Item:
    pay_rate = 0.8  # The pay rate with 20% discount
    all = []    # Append all the attribute values inside this list

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to receive arguments
        assert price >= 0, f'Price {price} should be greater than 0'
        assert quantity >= 0, f'Quantity {quantity} should be greater than 0'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        # for item in items:
        #     print(item)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # strike out zero after decimal
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # pay_scale is class attribute

    # This will give output of value of instance is created against class
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"

# child class inherited from parent class


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):

        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phone >= 0, f"Broken phone {broken_phone} should be greater than 0"

        # Assign to self object
        self.broken_phone = broken_phone


phone1 = Phone("samsung", 500, 5, 1)
print(phone1.calculate_total_price())
print(phone1.all)
