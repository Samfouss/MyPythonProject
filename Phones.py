import Item

class Phone(Item):

    def __init__(self, name:str, price:int, quantity=0):
        super().__init__(
            name, price, quantity
        )