from .abc_auto import ABCAuto

class Tata(ABCAuto):
    
    def start(self):
        print("Tata Running !!!!")
    
    def stop(self):
        print("Tata Stoping Down !!!!")