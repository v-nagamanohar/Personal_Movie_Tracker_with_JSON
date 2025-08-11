

---

## 🎬 My Movie DB

A simple Python-based command-line application to manage your personal movie database.  
You can add, view, and search movies with details like title, genre, and rating.  
The data is stored in a JSON file (`Movies.json`) for persistence.

---

## 📂 Features

- Add Movie: Save a movie with its title, genre, and rating (0–10).
- View All Movies: Display the list of movies in the database.
- Search Movies: Find movies by title or genre.
- Data Persistence: All data is stored in `Movies.json` so it stays even after program exit.

---

## 🛠 Requirements

- Python 3.10+
- No external libraries required (uses only built-in modules: `os` and `json`).

---

## 📜 How to Run

1. Clone or Download this script.
2. Open a terminal in the script's directory.
3. Run the script:

```bash
python movie_db.py
````

---

## 📋 Usage

After running the program, you’ll see the menu:

```
🍿 My Movie DB
1. Add Movie
2. View All Movies
3. Search Movie
4. Exit
```

### 1️⃣ Add Movie

 Enter the movie title, genre, and rating.
 Ratings must be between `0` and `10`.
 If the movie already exists, it won’t be added again.

### 2️⃣ View All Movies

 Displays all movies in the format:

```
title -- genre -- rating
```

### 3️⃣ Search Movie

 Search by title or genre (case-insensitive).
 Displays matching results with their details.

### 4️⃣ Exit

 Closes the application.

---

## 📁 File Structure

```
Movies.json     # Stores all movie data in JSON format
movie_db.py     # Main Python script
```

---

## 💡 Example

```
🍿 My Movie DB
1. Add Movie
2. View All Movies
3. Search Movie
4. Exit
Enter the option (1-4): 1
Enter the movie name: Inception
Genre: sci-fi
Enter rating(0-10): 9
Movie added ✅
```

---

## ⚠ Notes

 JSON file is automatically created when you add your first movie.
 Make sure to enter a valid rating between 0 and 10.
 Search is case-insensitive.

---

👨‍💻 Author: Naga Manohar
📅 Version: 1.0

```

