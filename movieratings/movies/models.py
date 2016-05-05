from django.db import models


class Ratings(models.Model):
    rater_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()


class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
