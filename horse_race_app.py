from core.horse_factory import HorseFactory
from horse_race import HorseRace
from jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_factory = HorseFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        try:
            horse = self.horse_factory.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse.__class__.__name__} horse {horse_name} is added."
        except RuntimeError:
            pass

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_last_horse_by_type(horse_type)

        return jockey.jockey_take_a_horse(horse)

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_name(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)

        return race.register_jockey_for_the_race(jockey)

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_name(race_type)
        return race.start_race()

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __find_last_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]

            if not horse.is_taken and horse.__class__.__name__ == horse_type:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __find_race_by_name(self, race_name):
        for race in self.horse_races:
            if race.race_type == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")