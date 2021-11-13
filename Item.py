import csv
from os import name


class Item:
    # This is class attributes. Attributes belong to class
    rate = 0.8
    all = []

    def __init__(self, name:str, price:int, quantity=0):
        # Valider les entrées
        assert price >= 0, f"Please the price {price} must be greather than zero"
        assert quantity >= 0, f"Please the quantity {quantity} must be greather than zero"
        
        # Assign to self objet the value of parameters : this is instance attributes
        # Belong to objects we create 
        self.__name = name
        self.price = price
        self.quantity = quantity

        # To append every instance of Item created
        Item.all.append(self)

    # Une méthode : fonction faisant partie de notre calss
    def calculate_total_price(self):
        return self.price*self.quantity

    # Methode to discount prices
    def apply_discount1(self):
        # But hear we can overwrite this rate instance
        self.price = self.price * self.rate
        # At this way we can note overwrite this variable rate
        # self.price = self.price * Item.rate

    # Receive csv file and instanciate objects. So it gonna work on class not on objet
    # It is a class method, which can be access only at class level
    # We use class method to instanciate our class from a particular data structure
    
    @property
    def name(self):
        # cette propriété nous permet de faire tout s qu'on veut une fois qu'on a l'attribut
        # Une fois  qu'on essaie d'avoir access à cet attribut, les codes dans cette fonction sont exécuté
        return self.__name
    
    @name.setter
    def name(self, value):
        # Ici lorsqu'on veut modifier un attribut, c'est cette fonction qui est exécutée
        self.__name = value

    @classmethod
    def instantiate_from_csv_file(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            #print(item)
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # This class method change the rate of the class define at the top
    @classmethod
    def change_rate(cls, rate_change):
        cls.rate = rate_change

    #@classmethod
    #def split_change_to_instance(cls, string_to_split):
    #    name, price, quantity = string_to_split.split('-')

    # we use static method if we want to something not related to instance   
    @staticmethod
    def is_integer(num):
        
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Use magic method to print the name of ours class when call it
    def __str__(self):
        pass 

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


#item1 = Item("Phone 1", 3, 19)
#print(item1.calculate_total_price())

# Print instances in class level
#print(Item.__dict__)
#print(item1.__dict__)

#for instance in Item.All:
#    print(instance.name)

#print(Item.all)

Item.instantiate_from_csv_file()
print(Item.all)

print(Item.is_integer(7.8))


