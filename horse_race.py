from core.validator import Validator
from jockey import Jockey


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.raises_if_string_not_in_list(value, 'Race type does not exist!')
        self.__race_type = value

    def register_jockey_for_the_race(self, jockey: Jockey):
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

        if any(j.name == jockey.name for j in self.jockeys):
            return f"Jockey {jockey.name} has been already added to the {self.race_type} race."

        self.jockeys.append(jockey)
        return f"Jockey {jockey.name} added to the {self.race_type} race."

    def start_race(self):
        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {self.race_type} needs at least two participants!")
        winner = sorted(self.jockeys, key=lambda j: j.horse.speed, reverse=True)[0]
        return f"The winner of the {self.race_type} race, with a speed of {str(winner.horse.speed)}km/h is {str(winner.name)}! Winner's horse: {winner.horse.name}."



