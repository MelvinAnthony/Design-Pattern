from abc import ABCMeta, abstractmethod

class IHouseBuilder(metaclass = ABCMeta):
    
    @abstractmethod
    def set_wall_meterial(self,value):
        pass
    
    @abstractmethod
    def set_building_type(Self,value):
        pass

    @abstractmethod
    def set_no_of_doors(self,value):
        pass

    @abstractmethod
    def set_no_of_windows(self,value):
        pass

    @abstractmethod
    def get_result(self):
        pass

class HouseBuilder(IHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_wall_meterial(self,value):
        self.house.wall_material = value
        return self

    def set_building_type(self,value):
        self.house.building_type = value
        return self

    def set_no_of_doors(self,value):
        self.house.no_of_doors = value
        return self

    def set_no_of_windows(self,value):
        self.house.no_of_windows = value
        return self

    def get_result(self):
        return self.house
    
class House():
    def __init__(self,building_type= "Appartment", doors = 5, wall_material = "Wood", windows = 50):
        self.wall_material = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return f"This is a {self.wall_material} {self.building_type} with {self.doors} door's and {self.windows} window's."
    
class IglooDirector():
    @staticmethod
    def constract():
        return HouseBuilder()\
        .set_building_type("Igloo")\
        .set_wall_meterial("Wood")\
        .set_no_of_doors(10)\
        .set_no_of_windows(20)\
        .get_result()

if __name__ == '__main__':
    igloo1 = IglooDirector.constract()

    print(igloo1)