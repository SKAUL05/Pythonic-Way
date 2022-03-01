from .abc_auto import ABCAuto


class Hyundai(ABCAuto):
    def start(self):
        print("Hyundai Running !!!!")

    def stop(self):
        print("Hyundai Stoping Down !!!!")
