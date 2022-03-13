from django.urls import path

from . import views

urlpatterns = [
    # ex. /people/
    path('', views.index, name='index'),
    # ex. /people/5/
    path('<int:character_id>/', views.detail, name="detail"),
]