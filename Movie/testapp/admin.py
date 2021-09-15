from django.contrib import admin
from .models import *


# Register your models here.

class Movie_Admin(admin.ModelAdmin):
    list_display = ['rdate', 'movie_name', 'hero', 'heroine']


admin.site.register(Movie_Model, Movie_Admin)
