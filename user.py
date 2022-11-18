import hashlib
from brta import BRTA
from vehicles import Car
from vehicles import Bike
from vehicles import Cng
from ride_manager import uber
from random import randint,choice
from threading import *
license_authority=BRTA()
class UserAllreadyExict(Exception):
    def __init__(self, email,*args: object) -> None:
        print(f"{email} user allready created")
        super().__init__(*args)
class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encrypted=hashlib.md5(password.encode()).hexdigest()
        already_created=False
        with open("users.txt",'r') as file:
            if email in file.read():
                already_created=True
                # raise UserAllreadyExict(email)
                
        file.close()
        if already_created==False:
            with open("users.txt",'a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
                    
            file.close()
            # print(self.name, "user created")
            
    @staticmethod
    def long_in(email,password):
        stored_password=""
        with open("users.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(" ")[1]
        file.close()
        hashed_password=hashlib.md5(password.encode()).hexdigest()
        if hashed_password==stored_password:
            print("vaild user")
            return True
        else:
            print("invild user")
            return False

class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location=location
        self.__trip_history=[]
        self.balance=balance
        super().__init__(name, email, password)

    def set_location(self,location):
        self.location=location
    def get_location(self):
        return self.location
  
    def start_a_trip(self, fare,trip_info):
        self.balance-=fare
        self.__trip_history.append(trip_info)
    def get_trip_history(self):
        return self.__trip_history

class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.license=license
        self.__trip_history=[]
        self.valid_driver=license_authority.validate_license(email,license)
        self.earning=0
        self.vehicle=None

    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result== False:
            # print("Sorry you failed, try again")
            self.license=None
        else:
            self.license=result
            self.valid_driver=True

    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            
            if vehicle_type=='car':
                self.vehicle=Car(vehicle_type,license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type=='bike':
                self.vehicle=Bike(vehicle_type,license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                self.vehicle=Cng(vehicle_type,license_plate, rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
        else:
            # print("You are not a valid driver")
            pass

    def start_a_trip(self,start,destiantion,fare,trip_info):
        self.earning+=fare   
        self.location=destiantion
        thred=Thread(target=self.vehicle.start_driving,args=(start,destiantion))
        thred.start()
        self.__trip_history.append(trip_info)


    def get_tirp_history(self):
        return self.__trip_history


rider1=Rider("rider1","rider1@gmail.com","1redir",randint(0,50),1000)
rider2=Rider("rider2","rider2@gmail.com","2redir",randint(0,50),5600)

rider3=Rider("rider3","rider3@gmail.com","3redir",randint(0,50),1000)
rider4=Rider("rider4","rider4@gmail.com","4redir",randint(0,50),5600)

rider5=Rider("rider5","rider5@gmail.com","5redir",randint(0,50),1000)
rider6=Rider("rider6","rider6@gmail.com","6redir",randint(0,50),5600)
vehicle_types=['cng','bike','car']
for i in range(1,100):
    driver1=Driver(f"driver{i}",f"driver{i}@gmail.com",f"{i}revird",randint(0,100),randint(10000,99999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicle_types),randint(10000,99999),10)


print(uber.get_available_cars())
uber.find_a_vehicle(rider1,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider4,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider5,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider6,choice(vehicle_types),randint(1,100))
# print(rider1.get_trip_history())