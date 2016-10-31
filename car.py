class Car(object):
    num_of_doors=4
    num_of_wheels=4
    def __init__(self,name='General',model='GM',car_type='saloon',speed=0):
        self.name=name
        self.model=model
        self.car_type=car_type
        self.speed=speed

        if self.name=='Porshe' or self.name=='Koenigsegg':
            self.num_of_doors=2
        elif self.car_type=='trailer':
            self.num_of_wheels= 8
        else:
            self
    def is_saloon(self):
        if self.car_type=='trailer':
            return False
        return True

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed
        return self

def Main():
    man = Car('MAN', 'Truck', 'trailer')
    parked_speed = man.speed
    print(parked_speed)
    moving_speed = man.drive(7).speed
    print(moving_speed)
    honda = Car('Honda')
    print(honda.num_of_doors)
    print(honda.num_of_wheels)
    print(honda.is_saloon())
    print(honda.drive(12))
if __name__ == '__main__':
    Main()
