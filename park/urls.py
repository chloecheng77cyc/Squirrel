from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('map/',views.map),
    path('sightings/',views.all_squirrels),
    path('sightings/<int:unique_squirrel_id>/',views.squirrel_edit),
    path('sightings/add/',views.squirrel.add),
]
