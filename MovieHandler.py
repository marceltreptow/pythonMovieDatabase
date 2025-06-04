import csv

# The Movie Handler class handles every interaction with movie database.
# It initializes by loading the csv file and storing the movie data in a
# dictionary (movies).
class MovieHandler:
    # Load all movies from the csv file into
    # the class attribute self.movies of the type dictionary
    def __load_movies(self):
        self.movies = []
        csv_path = 'movieData.csv'
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.movies.append({
                    'genre': row['genre'],
                    'title': row['title'],
                    'synopsis': row['synopsis']
                })

    # Class constructor class the loadMovies method
    def __init__(self):
        self.__load_movies()

    # Return all distinct existing genres
    def get_all_genres(self):
        all_genres = set()
        for movie in self.movies:
            all_genres.add(movie['genre'])
        return all_genres

    # Return all movies
    def get_movies(self):
        return self.movies

    # Return a dictionary entry that matches the provided title
    def get_movie(self, movie_title):
        result_movie = ""
        for movie in self.movies:
            if movie["title"] == movie_title:
                result_movie = movie
        return result_movie

    # Return all movies in a dictionary that match the provided genre
    def get_movies_by_genre(self, genre_name):
        genre_movies = []
        for movie in self.movies:
            if movie['genre'].lower() == genre_name.lower():
                genre_movies.append(movie)
        return genre_movies