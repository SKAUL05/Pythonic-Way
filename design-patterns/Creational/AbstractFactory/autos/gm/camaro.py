from autos.abs_auto import AbsAuto


class ChevyCamaro(AbsAuto):
    def start(self):
        print("ChevyCamaro Running Smoothly")

    def stop(self):
        print("ChevyCamaro Shutting Down")
