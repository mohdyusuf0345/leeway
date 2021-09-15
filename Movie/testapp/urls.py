from django.urls import path
from .views import *


urlpatterns = [
    path('home/', index_view),
    path('add/', add_movie),
    path('list/', list_movie),
]