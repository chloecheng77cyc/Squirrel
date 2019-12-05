from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('map/',views.map_squirrels),
    path('sightings/',views.all_squirrels),
    path('sightings/<int:unique_squirrel_id>/',views.edit_squirrel),
    path('sightings/add/',views.add_squirrel),
]
