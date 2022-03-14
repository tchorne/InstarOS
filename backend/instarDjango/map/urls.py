from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    # ex. /people/
    path('', views.map, name='map'),
    # ex. /people/5/
]