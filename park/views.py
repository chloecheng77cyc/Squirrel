from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random

from .models import Sighting






def sighting_map(request):
    sightings = Sighting.objects.order_by('?')[:100]
    context = {
        'sightings' : sightings,
    }
    return render(request, 'park/map.html', context)




# Create your views here.
