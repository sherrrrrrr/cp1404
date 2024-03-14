COLOUR_CODES = {
    "AliceBlue": "#F0F8FF",
    "BlueViolet": "#8A2BE2",
    "Brown": "#A52A2A",
    "DarkOrange": "#FF8C00",
    "FireBrick": "#B22222",
    "Gold": "#FFD700",
    "LimeGreen": "#32CD32",
    "MediumPurple": "#9370DB",
    "SlateBlue": "#6A5ACD",
    "Tomato": "#FF6347"
}


def main():
    while True:
        color_name = input("Enter a color name (or blank to stop): ").strip().title()

        if color_name == "":
            break

        if color_name in COLOUR_CODES:
            print(f"The hexadecimal code for {color_name} is {COLOUR_CODES[color_name]}")
        else:
            print("Invalid color name. Please try again.")


if __name__ == '__main__':
    main()
