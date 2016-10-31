class Car(object):
	num_of_doors = 4
	num_of_wheels = 4
	speed = 0

	def __init__(self,name='General',model='GM',car_type=None):
		self.name=name
		self.model=model
		self.car_type=car_type


		if self.name=='Porshe' or self.name=='Koenigsegg':
			self.num_of_doors = 2

		elif self.car_type=='trailer':
			self.num_of_wheels = 8
		else:
			self

	def is_saloon(self):
		if self.car_type is not 'trailer':
			return True
		else:
			return False

	def drive(self):
		if self.car_type is 'trailer':
			Car.speed = 77
		else:
			Car.speed = 1000

		return Car.speed

def Main():
    honda = Car('Honda')
    print(honda.num_of_doors)
    print(honda.num_of_wheels)
    print(honda.is_saloon())
    print(honda.drive())
if __name__ == '__main__':
    Main()
