from django.shortcuts import render
from django.http import HttpResponse

from superhero_project import super_people
from superhero_project.super_people.models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'super_people/index.html', context)