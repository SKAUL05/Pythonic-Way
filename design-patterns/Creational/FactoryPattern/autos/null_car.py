from .abc_auto import ABCAuto


class NullCar(ABCAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print(f"Unknown Car {self._carname} Not Found")

    def stop(self):
        pass
