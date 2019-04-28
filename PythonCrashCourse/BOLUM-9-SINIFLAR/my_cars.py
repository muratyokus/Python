from car import Car, ElectricCar


"""My writing code."""

my_car  = Car('vw', 'Transporter', 2008)
my_ecar = ElectricCar('tesla', 'model s', 2018)

print("\nMy car.")
my_car.get_descriptive_name()
my_car.read_odometer()

print("\nMy electric car.")
my_ecar.battery.describe_battery()
my_ecar.get_descriptive_name()
my_ecar.battery.get_range()


'''
my_beetle   = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla    = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
'''