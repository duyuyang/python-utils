class Car(object):
    def __init__(self, miles, color):
        self._miles = miles
        self._color = color

    @property
    def miles(self):
        return self._miles

    @property
    def color(self):
        return self._color

    def __str__(self):
        return f'Car: Miles{self.miles}, color={self.color}'

car1 = Car(miles=100, color='red')
print(car1)