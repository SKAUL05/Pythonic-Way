from autofactory import AutoFactory

factory = AutoFactory()

_CAR_NAMES = ['Maruti','Hyundai','Tata','Morris Garage']

for carname in _CAR_NAMES:
    car = factory.create_instance(carname=carname)
    car.start()
    car.stop()