from .unreliable_car import UnreliableCar

# Create a new unreliable car object, my_car, with name "Unreliable Car", 100 units of fuel and reliability of 50%
my_car = UnreliableCar("Unreliable Car", 100, 50)

# Test driving the unreliable car for 100 km
distance_driven = my_car.drive(100)

# Print the distance driven
print(f"Distance driven: {distance_driven}")