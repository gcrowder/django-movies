from django.contrib import admin

# Register your models here.
from .models import Rating, Movie

admin.site.register(Rating)
admin.site.register(Movie)
