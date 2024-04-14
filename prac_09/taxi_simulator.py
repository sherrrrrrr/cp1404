from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    bill_total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")

    while True:
        print(f"Bill to date: ${bill_total:.2f}")
        user_input = input(">>> ").lower()

        if user_input == "q":
            break
        elif user_input == "c":
            print("Taxis available:")
            for index, taxi in enumerate(taxis):
                print(f"{index} - {taxi}")
            choose_taxi = int(input("Choose taxi: "))
            if choose_taxi >= len(taxis) or choose_taxi < 0:
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[choose_taxi]
                print(f"Bill to date: ${bill_total:.2f}")
        elif user_input == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                bill_total += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                print(f"Bill to date: ${bill_total:.2f}")

            print(f"Total trip cost: ${bill_total:.2f}")
            print("Taxis are now:")
            for taxi in taxis:
                print(f"- {taxi}")

if __name__ == '__main__':
    main()
