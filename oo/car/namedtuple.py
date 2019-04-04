from collections import namedtuple

Car = namedtuple('Car', ['miles', 'color'])

car1 = Car(miles=100, color='red')

print(car1)

car1.miles = 200 # can't set attribute
