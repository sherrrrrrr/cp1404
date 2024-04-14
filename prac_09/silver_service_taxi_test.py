from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object, my_taxi, named "Hummer", with 200 units of fuel, price of $1.23 per km, and fanciness of 4
my_taxi = SilverServiceTaxi("Hummer", 200, 1.23, 4)

# Drive the SilverServiceTaxi for 18 km
my_taxi.drive(18)

# Calculate and print the fare
fare = my_taxi.get_fare()
print(f"The fare for the trip is: ${fare:.2f}")

# Test if the fare calculation is correct
assert fare == 48.78, "Fare calculation is incorrect"