from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):

        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phone >= 0, f"Broken phone {broken_phone} should be greater than 0"

        # Assign to self object
        self.broken_phone = broken_phone


