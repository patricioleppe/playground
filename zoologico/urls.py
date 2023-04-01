from django.urls import path
from .views import AnimalListView

animals_patterns = ([
    path('', AnimalListView.as_view(), name='animales'),
   
], 'animales')