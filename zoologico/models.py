from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class TypeAnimal(models.Model):
    type = models.CharField(max_length=50, verbose_name="Tipo")
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["type"]

    def __str__(self):
         return f"{self.type}"
    

class Animal(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    type = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    sound = models.CharField(max_length=30, verbose_name="Sonido")
    avatar = models.ImageField(upload_to='zoologico/', null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created_at = models.DateField(auto_now_add=True, verbose_name="Creacion")
    updated_at = models.DateField(auto_now_add=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"
        ordering = ["order","type"]

    def __str__(self):
         return f"{self.name} ({self.type}) "
    

