# benefits of abstraction and encapsulation
# Abstraction: hiding the implementation details and showing only the functionality
# Encapsulation: wrapping up of data and methods into a single unit called class
# Encapsulation is a way to achieve abstraction

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        print("Petrol Engine started")

    def stop(self):
        print("Petrol Engine stopped")

class DieselEngine(Engine):
    def start(self):
        print("Diesel Engine started")

    def stop(self):
        print("Diesel Engine stopped")

class Car(ABC):
    def __init__(self, make, model, engine: Engine):
        self.make = make
        self.model = model
        self._engine = engine

    @abstractmethod
    def drive(self):
        pass

    def start(self):
        self._engine.start()

    def stop(self):
        self._engine.stop()

    def get_description(self):
        return f"{self.make} {self.model}"
    
class PetrolCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model, PetrolEngine())

    def drive(self):
        print(f"Driving {self.get_description()} with petrol engine")

class DieselCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model, DieselEngine())

    def drive(self):
        print(f"Driving {self.get_description()} with diesel engine")

petrol_car = PetrolCar("Toyota", "Corolla")
petrol_car.start()
petrol_car.drive()
petrol_car.stop()

diesel_car = DieselCar("Toyota", "Innova")
diesel_car.start()
diesel_car.drive()
diesel_car.stop()

print(petrol_car.get_description()) # Toyota Corolla

# petrol_car._engine = DieselEngine() # AttributeError: can't set attribute
# petrol_car._engine.start() # AttributeError: can't set attribute

