from abc import ABC, abstractmethod

from core.validator import Validator


class Horse(ABC):
    MAXIMUM_SPEED = None
    SPEED_INCREMENTAL = None

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raises_if_string_is_less_than(value, 4, f'Horse name {value} is less than 4 symbols!')
        self.__name = value
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value > self.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass



