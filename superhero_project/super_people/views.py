from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'super_people/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'super_people/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase =request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('super_people:index'))
    else:
        return render(request, 'super_people/create.html')

def update(request, hero_id):
    if request.method == 'POST':
        update_hero = Superhero.objects.get(pk=hero_id)
        update_hero.name = request.POST.get('name')
        update_hero.alter_ego = request.POST.get('alter_ego')
        update_hero.primary = request.POST.get('primary')
        update_hero.secondary = request.POST.get('secondary')
        update_hero.catchphrase = request.POST.get('catchphrase')
        update_hero.save()
        return detail(request, hero_id)
    else:
        update_hero = Superhero.objects.get(pk=hero_id)
        context = {
            'update_hero': update_hero
        }
        return render(request, 'super_people/update.html', context)

def delete(request, hero_id):
    if request.method == 'POST':
        details = Superhero.objects.get(pk=hero_id)
        details.delete()
        return HttpResponseRedirect(reverse('super_people:index'))
    else:
        details = Superhero.objects.get(pk=hero_id)
        context = {
            'hero': details
        }
        return render(request, 'super_people/delete.html', context)
