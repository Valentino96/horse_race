from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    horse_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def create_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.horse_types:
            raise RuntimeError('Invalid type!')
        return self.horse_types[horse_type](horse_name, horse_speed)
