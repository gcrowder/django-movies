import pandas as pd
from movies.models import Ratings

Ratings.objects.all().delete()

df = pd.read_csv('../ml-10M100K/ratings.dat', delimiter='::', header=None,
                 names=['rater_id', 'movie_id', 'rating', 'time'])
for row in df.iterrows():
    row_dict = row[1].to_dict()
    rate = Ratings(rater_id=int(row_dict['rater_id']),
                   movie_id=int(row_dict['movie_id']),
                   rating=int(row_dict['rating']))
    rate.save()
