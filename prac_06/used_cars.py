from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    limo_drive_distance = limo.drive(115)

    print(f"Amount of fuel in {limo.name}: {limo.fuel}")
    print(f"Distance driven by {limo.name}: {limo_drive_distance}")
    print(limo)

main()