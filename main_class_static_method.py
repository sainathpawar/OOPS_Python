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
        return f"Item('{self.name}, {self.price}, {self.quantity}')"


# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.5))

'''
Note:

StaticMethod : Method which is nothing to do with the instance created by class. 
               therefore it does not pass class as reference object.

'''
