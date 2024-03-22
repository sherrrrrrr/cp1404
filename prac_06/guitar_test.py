from guitar import Guitar


def test_methods():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500.00)

    current_year = 2022

    expected_gibson_age = 100
    actual_gibson_age = gibson.get_age(current_year)
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {actual_gibson_age}")
    if actual_gibson_age != expected_gibson_age:
        print(f"{gibson.name} get_age() - NotMatch!")

    expected_another_guitar_age = 9
    actual_another_guitar_age = another_guitar.get_age(current_year)
    print(f"{another_guitar.name} get_age() - Expected {expected_another_guitar_age}. Got {actual_another_guitar_age}")
    if actual_another_guitar_age != expected_another_guitar_age:
        print(f"{another_guitar.name} get_age() - NotMatch!")

    expected_gibson_vintage = True
    actual_gibson_vintage = gibson.is_vintage(current_year)
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {actual_gibson_vintage}")
    if actual_gibson_vintage != expected_gibson_vintage:
        print(f"{gibson.name} is_vintage() - NotMatch!")

    expected_another_guitar_vintage = False
    actual_another_guitar_vintage = another_guitar.is_vintage(current_year)
    print(
        f"{another_guitar.name} is_vintage() - Expected {expected_another_guitar_vintage}. Got {actual_another_guitar_vintage}")
    if actual_another_guitar_vintage != expected_another_guitar_vintage:
        print(f"{another_guitar.name} is_vintage() - NotMatch!")


test_methods()
