from abc import ABC, abstractclassmethod
import time
class Vehicle(ABC):
    speed={
        "car": 30,
        "bike": 50,
        "cng": 15
    }
    def __init__(self,vehicle_type, rate,driver,license_plate) -> None:
        self.vehicle_type=vehicle_type
        self.rate=rate
        self.license_plate=license_plate
        self.driver=driver
        self.status= "available"
        self.speed=self.speed[vehicle_type]
    @abstractclassmethod
    def start_driving(self):
        pass
    @abstractclassmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type,license_plate, rate, driver ) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    def start_driving(self,start,destination):
        self.status="unavailable"
        print(self.vehicle_type, self.license_plate, "started")
        destance=abs(start-destination)
        for i in range(0,destance):
            time.sleep(0.5)
            print(f"Driving: {self.license_plate} current location {i} of {destance}\n")

        self.trip_finished()

    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type, self.license_plate, "completed trip")

class Bike(Vehicle):
    def __init__(self, vehicle_type ,license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    def start_driving(self,start,destination):
        self.status="unavailable"
        print(self.vehicle_type, self.license_plate, "started")
        destance=abs(start-destination)
        for i in range(0,destance):
            time.sleep(0.5)
            print(f"Driving: {self.license_plate} current location {i} of {destance}\n")

        self.trip_finished()
    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type, self.license_plate, "completed trip")

class Cng(Vehicle):
    def __init__(self, vehicle_type,license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    def start_driving(self,start,destination):
        self.status="unavailable"
        print(self.vehicle_type, self.license_plate, "started")
        destance=abs(start-destination)
        for i in range(0,destance):
            time.sleep(0.5)
            print(f"Driving: {self.license_plate} current location {i} of {destance}\n")

        self.trip_finished()

    def trip_finished(self):
        self.status="available"
        print(self.vehicle_type, self.license_plate, "completed trip")