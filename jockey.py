from core.validator import Validator
from horse_specification.horse import Horse


class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raises_if_string_is_empty(value, 'Name should contain at least one character!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.if_number_is_less_than(value, 18, 'Jockeys must be at least 18 to participate in the race!')
        self.__age = value

    def jockey_take_a_horse(self, horse:Horse):
        if self.horse is None:
            horse.is_taken = True
            self.horse = horse
            return f"Jockey {self.name} will ride the horse {horse.name}."
        return f"Jockey {self.name} already has a horse."