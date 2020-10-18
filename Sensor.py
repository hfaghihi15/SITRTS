class Sensor:
    def __init__(self, _name):
        self.name = _name


class SensorShot(Sensor):
    def __init__(self, _name, _value=None):
        super().__init__(_name)
        self.value = _value
