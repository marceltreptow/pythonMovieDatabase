Report for Python project:

Code implementation:
Moviehandler.py:


UserInteractionHandler.py:
The “UserInteractionHandler” script is the user interface for the movie recommendation system. Its main role is to guide the user through selecting a preferred genre and displaying a list of corresponding movies retrieved via the “MovieHandler” class.
The script begins by instantiating the “Moviehandler” object, which loads movie data from the CSV file. It then retrieves and displays a sorted list of available genres to the user. After prompting the user for a genre, the program performs input validation to make sure the genre exists in the CSV file. If the user input is valid, the movies and synopsis available in that genre will be listed, if not valid the user will receive an error message.

Result:
After the completion of the code the program successfully lists all available movies, genres and synopsis. The program prompts the user to input a genre of the available selection. If the genre is not in the csv list the program will give the user an error message. The program is able to read the CSV file and match genres regardless of casing improving usability.

Lessons learned:
1.	The importance of case handling: initially, genre input was case-sensitive, which caused      valid user inputs like “drama” instead of “Drama” to fail. Fixing this made the program       user-friendly.
2.	Error checking and input validation: Adding feedback for incorrect inputs enhanced the        overall reliability of the program.
3.	Working with CSV files: Understanding row parsing was essential.


