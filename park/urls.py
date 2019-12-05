from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('map/',views.map),
    path('<int:unique_squirrel_id>/',views.squirrel_edit),
    path('add/',views.squirrel.add),
]
