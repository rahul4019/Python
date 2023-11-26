class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# INHERITANCE

# overriding the moves method of class the Vehicle


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # inherits make and model from the Vehicle class
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

# inheriting everthing from the Vehicle class


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfWagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfWagon.get_make_model()
golfWagon.moves()

print('\n\n')

# POLYMORPHISM
# Polymorphism in Python refers to the ability of a single function, method, or operator to work with different types of data or objects. It allows objects of different types to be treated as objects of a common type

for v in (my_car, your_car, cessna, mack, golfWagon):
    v.get_make_model()
    v.moves()

