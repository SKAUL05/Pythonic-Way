from autos.abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    def start(self):
        print("Ford Fiesta Running Cheaply")

    def stop(self):
        print("Ford Fiesta Shutting Down")
