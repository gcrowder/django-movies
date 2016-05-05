# django-movies
This is an exercise to turn the movie lens data set into a django-based web app. Currently, only the models of the app are complete.

## movies.models
[models.py](https://github.com/gcrowder/django-movies/blob/master/movieratings/movies/models.py) contains the models used to create the database tables. There are two tables: Movie and Rating. Movie contains Movie IDs and respective movie titles. Rating contains User IDs, the ID of the movie rated and that users rating for that movie.

## read_in_data
[read_in_data.py](https://github.com/gcrowder/django-movies/blob/master/movieratings/read_in_data.py) contains the code that reads the movie lens dataset into the database using the django models. The files are double-colon (::) delimited and I use pandas to read the data and use the django model classes to create and save Movie and Rating objects to their respective tables. This script uses get_or_create to ensure that no duplicate entries are made to the database.
