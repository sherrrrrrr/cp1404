from guitar import Guitar


def main():
    guitars = []

    # Uncomment the following lines to manually input guitar details
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitars.append(Guitar(name, year, cost))

    # Uncomment the following lines to use sample guitar data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print("\nMy guitars!")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()