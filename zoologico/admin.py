from django.contrib import admin
from .models import Animal, TypeAnimal

# Register your models here.

admin.site.register([Animal, TypeAnimal])
