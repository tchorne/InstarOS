from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [
    # ex. /people/
    path('', views.index, name='index'),
    # ex. /people/5/
    path('<int:character_id>/', views.detail, name="detail"),

    path('<int:character_id>/submitNote', views.submitNote, name="note"),

    path('notes/<int:note_id>/delete', views.deleteNote, name="delNote")
]