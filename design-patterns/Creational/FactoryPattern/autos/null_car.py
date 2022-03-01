from .abc_auto import ABCAuto

class NullCar(ABCAuto):
    
    def __init__(self, carname):
        self._carname = carname
    
    def start(self):
        print("Unknown Car {} Not Found".format(self._carname))
    
    def stop(self):
        pass