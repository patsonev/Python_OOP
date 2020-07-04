class Cup:
    current_quantity = 0

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity < self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())