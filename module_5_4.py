class House:
    
    houses_history = []
    
    def __new__(cls, *args, **kwargs):
         if args:
            building_name = args[0]
            cls.houses_history.append(building_name)
            instance = super().__new__(cls)
            return instance
    
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    
    def __len__(self):
        return self.number_of_floors
    
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
            return True
    
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    
    def __add__(self, value):
        if isinstance(value, (int, float)):
            self.number_of_floors += value
            return self
    
    def __radd__(self, value):
            return self.__add__(value)

    def __iadd__(self, value):
            return self.__add__(value)
        
    def __str__(self):
            return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
