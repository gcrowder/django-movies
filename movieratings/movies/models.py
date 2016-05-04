from django.db import models


class Rater(models.Model):
    rater_id = models.IntegerField()
    ratings = models.ForeignKey(Ratings, on_delete=models.CASCADE)


class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    ratings = models.ForeignKey(Ratings, on_delete=models.CASCADE)


class Ratings(models.Model):
    rater_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()
