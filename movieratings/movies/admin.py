from django.contrib import admin

# Register your models here.
from .models import Ratings, Rater, Movies

admin.site.register(Ratings)
admin.site.register(Rater)
admin.site.register(Movies)
