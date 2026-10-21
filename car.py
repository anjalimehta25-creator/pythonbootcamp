class car:
    def __init__(self,brand,speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self,amount):
        self.amount = amount
        self.speed = self.speed + amount
        print(self.speed)

    def brake(self,amount):
        self.amount = amount
        if self.speed > amount:
           self.speed = self.speed - amount
           print(self.speed)
        else:
            self.speed = 0


car1 = car("BMW")
print(car1.brand)
car1.accelerate(50)
car1.brake(20)
