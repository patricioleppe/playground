from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Esta funcion es para eliminar el archivo imagen, cuando se cambia la imagen del perfil
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
        


class Profile(models.Model):
    # Crear una relación uno a uno entre el usuario y el perfil.
    # on_delete=models.CASCADE Significa que si se elimina el usuario, también se eliminará el perfil.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Está creando un campo en la base de datos que almacenará la ruta a la imagen.
    avatar = models.ImageField(upload_to=custom_upload_to , null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta():
        ordering = ['user__username']

# Es un decorador que le dice a Django que llame a la 
# función que le sigue después de guardar un objeto Usuario.
@receiver(post_save, sender=User)

def ensure_profile_exists(sender, instance, **kwargs):
    # Si se crea un usuario, obtenga o cree un perfil para ese usuario
    if kwargs.get('created', False):    
        # Es un atajo para obtener o crear un perfil para el usuario dado.
        Profile.objects.get_or_create(user=instance)
        # print("se acaba de crear un usuario y su perfil enlazado")


