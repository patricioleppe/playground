from django import forms
from .models import Animal, TypeAnimal

class AnimalForm(forms.ModelForm):

    typeAnimals = [(c.type) for c in TypeAnimal.objects.all()]
    typeAnimal = forms.ChoiceField(choices=typeAnimals)
    class Meta:
        model = Animal
        fields = ['name', 'typeAnimal', 'sound', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'typeAnimal': forms.ChoiceField(),
            'sound': forms.TextInput(attrs={'class':'form-control'}),
            'avatar': forms.ImageField(),
        }

        labels = {
            'name': '', 'typeAnimal': '', 'sound' : '', 'avatar':''
        }
