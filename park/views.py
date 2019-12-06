from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random

from .models import Squirrel
from .forms import SquirrelForm


def map_squirrels(request):
    squirrels = Squirrel.objects.order_by('?')[:100]
    context = {
        'squirrels' : squirrels,
    }
    return render(request, 'park/map.html', context)


def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'park/all.html', context)


def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/park/sightings/add/')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'park/edit.html',context)


def edit_squirrel(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(id=unique-squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique-squirrel-id}')
    elif request.method=='DELETE':
        squirrel.delete()
        return redirect(f'/sighting_list/{unique-squirrel-id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form':form,
    }

    return render(request, 'park/edit.html', context)



def stats_squirrel(request):
    count = Squirrel.objects.all().count()

    
    activities = dict()
    activities['running'] = Squirrel.objects.filter(Running=True).count()
    activities['chasing'] = Squirrel.objects.filter(Chasing=True).count()
    activities['climbing'] = Squirrel.objects.filter(Climbing=True).count()
    activities['eating'] = Squirrel.objects.filter(Eating=True).count()
    activities['foraging'] = Suirrel.objects.filter(Foraging=True).count()

    sorted_activities = sorted(activities.items(), key=lambda kv: kv[1], reverse=True)
    most_common_activity = sorted_activities[0][0]
    most_common_activity_count = sorted_activities[0][1]

    
    count2 = Squirrel.objects.filter(Age='Adult').count()+Squirrel.objects.filter(Age='Juvenile').count()
    adult_percentage = round(Squirrel.objects.filter(Age='Adult').count()/count2,2)
    juvenile_percentage = round(Squirrel.objects.filter(Age='Juvenile').count()/count2,2)


    interactions = dict()
    interactions['approaches'] = Squirrel.objects.filter(Approaches=True).count()
    interactions['indifferent'] = Squirrel.objects.filter(Indifferent=True).count()
    interactions['runs_from'] = Squirrel.objects.filter(Runs_from=True).count()

    sorted_interactions = sorted(interactions.items(), key=lambda kv: kv[1], reverse=True)
    most_common_interaction = sorted_interactions[0][0]
    most_common_interaction_count = sorted_interactions[0][1]


                                                                                                
    

    context = {
        'count' : count,
        'adult_percentage' : adult_percentage,
        'juvenile_percentage': juvenile_percentage
        'most_commmon_activity' : most_common_activity,
        'most_common_activity_count' : most_common_activity_count,
        'most_common_interaction' : most_common_interaction,
        'most_common_interaction_count' : most_common_interaction_count,
    }
    
    return render(request, 'park/stats.html/', context)
                                                                                                                                                                         


# Create your views here.
