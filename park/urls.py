from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('map/',views.map_squirrels,name='map_squirrels'),
    path('sightings/',views.all_squirrels,name='all_squirrels'),
    path('sightings/<str:unique_squirrel_id>/',views.edit_squirrel,name='edit_squirrel'),
    path('sightings/add/',views.add_squirrel,name='add_squirrel'),
    path('sightings/stats/',views.stats_squirrel,name='stats_squirrel'),
]
