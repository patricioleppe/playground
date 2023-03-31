from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    # Crear un nuevo campo en el formulario llamado `email` y es `forms.EmailField`, lo que significa
    # que es un campo que solo acepta direcciones de correo electrónico.
    # Creando un nuevo campo en el formulario llamado email.
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        # Decirle a Django que UserCreationFormWithEmail es un formulario para el modelo de Usuario.
        model= User
        fields = ("username", "email", "password1", "password2")
    
    def clean_email(self):
        
        # Obtener el correo electrónico del formulario.
        email = self.cleaned_data.get("email")
        
        # Comprobando si el correo electrónico ya está registrado.
        if User.objects.filter(email=email).exists():
            # Generando un error si el correo electrónico ya está registrado.
            raise forms.ValidationError("El Correo ya esta registrado...")    
        return email
    

# perfil usuario
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control mt-3'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link' : forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder':'Enlace'}),

        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        # Comprobando si el campo de correo electrónico está en 
        # el diccionario de datos cambiados.
        if 'email' in self.changed_data:
            # Está comprobando si el correo electrónico ya 
            # está registrado en la base de datos.
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El Correo ya esta registrado...")    
        return email