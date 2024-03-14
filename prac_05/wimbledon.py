def main():
    champions_data = read_file("wimbledon.csv")
    champion_wins = count_champion_wins(champions_data)
    countries = list_countries_of_champions(champions_data)
    display_champion_wins(champion_wins)
    display_countries_of_champions(countries)


def read_file(filename):
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            champions_data.append(line.strip().split(','))
    return champions_data


def count_champion_wins(champions_data):
    score = {}
    for champion in champions_data:
        name = champion[2]
        score[name] = score.get(name, 0) + 1
    return score


def list_countries_of_champions(champions_data):
    countries = set()
    for champion in champions_data:
        countries.add(champion[1])
    sorted_countries = sorted(countries)
    return sorted_countries


def display_champion_wins(champion_wins):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_wins.items()):
        print(f"{champion} {count}")


def display_countries_of_champions(countries):
    print("\nThese countries have won Wimbledon:")
    countries_string = ', '.join(countries)
    print(countries_string)


if __name__ == '__main__':
    main()
