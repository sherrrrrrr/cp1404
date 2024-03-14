STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
    "WA": "Western Australia",
    "NT": "Northern Territory",
    "ACT": "Australian Capital Territory"
}


def main():
    short_state = input("Enter state abbreviation: ").upper()

    full_state_name = STATE_NAMES.get(short_state)
    if full_state_name:
        print(f"The full state name for {short_state} is {full_state_name}")
    else:
        print("Invalid state abbreviation.")


if __name__ == '__main__':
    main()
