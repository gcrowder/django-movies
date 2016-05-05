import pandas as pd
from movies.models import Rating, Movie

# Rating.objects.all().delete()

df = pd.read_csv('../ml-10M100K/ratings.dat', delimiter='::', header=None,
                 names=['rater_id', 'movie_id', 'rating', 'time'])
for row in df.iterrows():
    row_dict = row[1].to_dict()
    obj, created = Rating.objects.get_or_create(rater_id=row_dict['rater_id'],
                                                movie_id=row_dict['movie_id'],
                                                rating=row_dict['rating'])

movie = pd.read_csv('../ml-10M100K/movies.dat', delimiter='::', header=None,
                    names=['movie_id', 'title', 'genre'])
for row in movie.iterrows():
    movie_dict = row[1].to_dict()
    obj, created = Movie.objects.get_or_create(movie_id=movie_dict['movie_id'],
                                               title=movie_dict['title'])
