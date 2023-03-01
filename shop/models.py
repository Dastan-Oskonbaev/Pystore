class Product:
    def __init__(self, name: str, color:str, memory:int, brand:str, model, price, category):
        self.name = name
        self.color = color
        self.memory = memory
        self.brand = brand
        self.model = model
        self.price = price
        self.category = category



class Category:
    def __init__(self, name:str):
        self.name = name
