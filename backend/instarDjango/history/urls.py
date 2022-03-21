from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    # ex. /people/
    path('', views.index, name='index'),
    # ex. /people/5/
    path('<int:event_id>/', views.detail, name="detail"),
]