import csv

class MovieHandler:
    def __loadMovies(self):
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

    def __init__(self):
        self.__loadMovies()

    def getAllGenres(self):
        all_genres = set()
        for movie in self.movies:
            all_genres.add(movie['genre'])
        return all_genres

    def getMovies(self):
        return self.movies

    def printMovies(self):
        for movie in self.movies:
            print(movie)

    def getMovie(self, movie_title):
        result_movie = ""
        for movie in self.movies:
            if movie["title"] == movie_title:
                result_movie = movie
        return result_movie

moviehandler = MovieHandler()
#print(moviehandler.getAllGenres())
#print(moviehandler.getMovies())
#moviehandler.printMovies()
print(moviehandler.getMovie("The godfather"))
