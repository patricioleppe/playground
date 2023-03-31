from django.shortcuts import get_object_or_404
from .models import Animal

# Create your views here.

def mi_vista(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)