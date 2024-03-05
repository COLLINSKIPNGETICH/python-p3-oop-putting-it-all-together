class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 1:
            self._discount = value
        else:
            raise ValueError("Discount must be between 0 and 1")

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount)
        return round(discounted_price, 2)

