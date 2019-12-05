from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random

from .models import Sighting


def map(request):
    sightings = Sighting.objects.order_by('?')[:100]
    context = {
        'sightings' : sightings,
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




# Create your views here.
