from horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    SPEED_INCREMENTAL = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.MAXIMUM_SPEED, self.speed+self.SPEED_INCREMENTAL)
        return self.speed
