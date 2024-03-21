import csv

WATCHED = 'w'
UNWATCHED = 'u'


# Function to load movies from a CSV file into a list of lists
def load_movies(filename='movies.csv'):
    movies = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies


# Function to display a welcome message with the name
def display_welcome_message(movies):
    print(f"Movies2See 1.0 - by JiaxinLi")
    watched_count = sum(1 for movie in movies if movie[3] == WATCHED)
    print(f"{len(movies)} movies loaded")


# Function to display the menu options
def display_menu():
    print("Menu")
    print("D - Display movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")


# Function to display the list of movies with details
def display_movies(movies):
    watched_count = 0
    for idx, movie in enumerate(movies):
        title, year, category, status = movie
        watched = "" if status == WATCHED else "*"
        print(f"{idx}. {watched} {title} - {year} ({category})")
        if status == WATCHED:
            watched_count += 1
    print(f"{watched_count} movies watched, {len(movies) - watched_count} movies still to watch")

# Function to add a new movie to the list
def add_movie(movies):
    title = input("Title: ")
    year = input("Year: ")
    category = input("Category: ")
    if not title or not year or not category:
        print("Input can not be blank, year must be a number.")
    else:
        movies.append([title, year, category, UNWATCHED])
        print(f"{title} ({category} from {year}) added to movie list")


# Function to mark a movie as watched
def watch_movie(movies):
    idx = int(input("Enter the number of a movie to mark as watched: "))
    if 0 <= idx < len(movies):
        if movies[idx][-1] == UNWATCHED:
            print(f"{movies[idx][0]} from {movies[idx][1]} watched")
            movies[idx][-1] = WATCHED
        else:
            print(f"You have already watched {movies[idx][0]}")
    else:
        print("Invalid movie number")


# Main program
def main():
    movies = load_movies()
    display_welcome_message(movies)

    while True:
        display_menu()
        choice = input("~ ").lower()

        if choice == 'd':
            display_movies(movies)
        elif choice == 'a':
            add_movie(movies)
        elif choice == 'w':
            watch_movie(movies)
        elif choice == 'q':
            with open('movies.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(movies)
            print(f"{len(movies)} movies saved to movies.csv\nHave a nice day :)")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()
