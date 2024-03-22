from programming_language import ProgrammingLanguage
import csv


def main():
        languages = []
        with open('languages.csv', 'r', newline='') as in_file:
            in_file.readline()
            for line in csv.reader(in_file):
                try:
                    name, typing, reflection, year, *extra_fields = line
                    reflection = reflection == "Yes"
                    year = int(year)
                    if extra_fields:
                        pointer_arithmetic = extra_fields[0] == "Yes"
                    else:
                        pointer_arithmetic = False  # Set default value if pointer arithmetic field is missing

                    language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
                    languages.append(language)
                except (ValueError, IndexError):
                    print(f"Ignore invalid line: {line}")

            for language in languages:
                print(language)


if __name__ == "__main__":
    main()
