from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

# Esta clase es un administrador del modelo Thread. Es un administrador porque hereda de
# models.Manager. Es un administrador para el modelo Thread porque se llama ThreadManager
class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # Filtrando los hilos que tienen ambos usuarios.
        queryset = self.filter(users = user1).filter(users = user2)
        # Comprobando si el conjunto de consultas tiene algún elemento.
        if len(queryset) > 0:
            # `queryset[0]` devuelve el primer elemento del conjunto de consultas.
            return queryset[0]
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages =  models.ManyToManyField(Message)

    objects = ThreadManager()

def messages_changed(sender, **kwargs):
    # Si se agrega un mensaje a una conversación y el usuario 
    # que envió el mensaje no está entre los
    # usuarios de la conversación, agregue el usuario a 
    # los usuarios de la conversación.
    
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action , pk_set)

    false_pk_set = set()    

    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
                    # `instance.users.all()` es un conjunto de consultas 
                    # que contiene todos los usuarios en el hilo.
            if msg.user not in instance.users.all():
                print("Hey! ({}) no forma parte del hilo!!!".format(msg.user))
                # Adición de la clave principal del mensaje a un conjunto.
                false_pk_set.add(msg_pk)
    
    # buscar los mensaje de false_pk_set que no esta en pk_set 
    # y los borramos de pk_set.
    # Está eliminando los mensajes que no pertenecen al hilo.
    pk_set.difference_update(false_pk_set)
                 
# Conectando la función `messages_changed` a la señal `m2m_changed`.
            # `Thread.messages.through` es el modelo intermedio 
            # que se utiliza para almacenar
            # la relación de muchos a muchos.
m2m_changed.connect(messages_changed, sender=Thread.messages.through)   

