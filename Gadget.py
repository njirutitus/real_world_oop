class Gadget:
    """A class used for modelling Gadgets in a web shop.."""
    """meant to bring more understanding to python classes"""
    __weight = 100
    __operating_system = None
    __battery_capacity = 2000
    __screen_size = 1
 
    def __init__(self, weight, operating_system, battery_capacity, screen_size):
        self.__weight = weight
        self.__operating_system = operating_system
        self.__battery_capacity = battery_capacity
        self.__screen_size = screen_size
 
    def get_weight(self):
        return self.__weight
 
    def set_weight(self, weight):
        self.__weight = weight
 
    weight = property(get_weight, set_weight)
 
    @property
    def operating_system(self):
        return self.__operating_system
 
    @operating_system.setter
    def operating_system(selg, new_os):
        self.__operating_system = new_os
