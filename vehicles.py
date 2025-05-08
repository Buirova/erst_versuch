class Vehicle:
    def drive(self):
        print("Vehicle is moving")

# Train
class Train(Vehicle):
    def drive(self):
        print("Train is moving on rails")

#  Car
class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road")

#  Car
class Cabrio(Car):
    def drive(self):
        print("Cabrio is driving with the top down")

class Kombi(Car):
    def drive(self):
        print("Kombi is driving with extra trunk space")

class SUV(Car):
    def drive(self):
        print("SUV is driving off-road")

# polymorphy
vehicles = [Train(), Cabrio(), Kombi(), SUV()]

for v in vehicles:
    v.drive()
   

     