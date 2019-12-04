from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('map/',views.map),
]
