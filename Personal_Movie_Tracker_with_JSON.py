import os
import json

FILE_NAME = "Movies.json"

def load_movies():
    if not os.path.exists(FILE_NAME): # checks whether file exists or not
        return []
    with open(FILE_NAME,'r',encoding='utf-8') as file:
        return json.load(file)
    
def save_movies(movies):
    with open(FILE_NAME,'w',encoding='utf-8') as file:
        json.dump(movies,file,indent=2)  

 
def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()

    if any(movie['title'].lower() == title for movie in movies):
        print("Movie already exists")
        return
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter rating(0-10)"))
        if not (0 <= rating <=10):
            raise ValueError
    except ValueError:
        print("Please Enter Valid Rating")
        return
    
    movies.append({"title":title,"genre":genre,"rating":rating})
    save_movies(movies)
    print("Movie added ✅")


def view_movies(movies):
    if not movies:
        print("No Movies in DB")
        return
    print("-"*30)
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
    print("-"*30)


def search_movies(movies): 
    term = input("Enter the title or genre: ").strip().lower()

    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()
    ]

    if not results:
        print("No matching result")
        return
    print(f"Found {len(results)} result's")
    for movie in results:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")


def run_movie_db():
    movies = load_movies()

    while True:
        print("\n🍿 My Movie DB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice = input("Enter the option (1-4): ").strip()
        match choice:
            case "1":
                add_movies(movies)
            case "2":
                view_movies(movies)
            case "3":
                search_movies(movies)
            case "4":
                print("Exiting the Movies DB")
                break
            case _:
                print("Enter Valid Choice")

if __name__ == "__main__":
    run_movie_db()

