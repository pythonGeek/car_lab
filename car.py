class Car(object):
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0
    def __init__(self, name= 'General', model = 'GM', car_type = None):
        self.name = name
        self.model = model
        self.car_type = car_type

        if self.name == "Koenigsegg" or self.name == "Porshe":
            self.num_of_doors = 2
        elif self.car_type == "trailer":
            self.num_of_wheels = 8
        else:
            pass

        def is_saloon(self):
            if self.car_type is not 'trailer':
                return True
            return False

        def drive(self, new_speed):
            if self.car_type is "trailer":
                return self.new_speed * 77/7
            else:
                return self.new_speed * 1000/3

def Main():
    honda = Car('Honda')
    print(honda.is_saloon())
if __name__ == '__main__':
    Main()
