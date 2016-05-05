from django.db import models


class Rating(models.Model):
    rater_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
