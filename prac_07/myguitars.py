from guitar import Guitar


def main():
    file_name = 'guitars.csv'
    guitars = load_guitars(file_name)

    print("All Guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("\nSorted Guitars (Oldest to Newest):")
    for guitar in guitars:
        print(guitar)

    new_guitar_name = input("Enter the name of your new guitar: ")
    new_guitar_year = int(input("Enter the year of your new guitar: "))
    new_guitar_cost = float(input("Enter the cost of your new guitar: "))
    new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
    guitars.append(new_guitar)

    save_guitars(file_name, guitars)
    print("\nNew guitar added and saved to file.")


def load_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def save_guitars(file_name, guitars):
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()