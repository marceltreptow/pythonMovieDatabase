from MovieHandler import MovieHandler

def main():
    mh = MovieHandler()

    # Get a sorted list of all available genres
    genres = sorted(mh.get_all_genres())

    print("Choose a genre and get a movie\n")

    # Checks if any genres is available
    if not genres:
        print("No genres available")
        return

    # Displays available genres to the user
    print("Available Genres:")
    for genre in genres:
        print(f"- {genre}")

    # Asks for user input
    selected_genre = input("\nEnter your preferred genre: ").strip()

    # Checks if the genre exist and stops the program if it does not
    # Case sensitive check
    if selected_genre not in [g.lower() for g in genres]:
        print(f"{selected_genre} is not a valid genre")
        return


    # Gets the list of movies based on the selected genre
    recommended = mh.get_movies_by_genre(selected_genre)

    # Prints movies titles and synopsis in the selected genre
    print(f"\nMovies in the {selected_genre} genre:")
    for movie in recommended:
        print(f"Title: {movie['title']}")
        print(f"Synopsis: {movie['synopsis']}\n")

if __name__ == "__main__":
    main()
