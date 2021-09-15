from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index_view(request):
    return render(request, 'testapp/home.html')


def add_movie(request):
    form = Movie_Form()
    if request.method == 'POST':
        form = Movie_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'testapp/addmovie.html', {'form': form})


def list_movie(request):
    movie_list = Movie_Model.objects.all()
    return render(request, 'testapp/listmovie.html', {'movie_list': movie_list})
