from django.urls import path
from .views import movie_list, actors, create_movie, movie_details, edit_movie, delete_movie, movie_actors

urlpatterns = [
    path('list', movie_list, name='movie_list'),
    path('actors', actors, name='actors'),
    path('get/<int:id>/actors', movie_actors, name='movie_actors'),
    path('details/<int:id>', movie_details, name='details'),
    path('create', create_movie, name='create'),
    path('edit/<int:id>', edit_movie, name='edit'),
    path('delete/<int:id>', delete_movie, name='delete')
]
