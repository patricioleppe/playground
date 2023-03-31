from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

class SignUpView(CreateView):
    # Diciéndole a Django que use la clase UserCreationFormWithEmail como formulario para esta vista.
    form_class = UserCreationFormWithEmail
    # Diciéndole a Django que use la plantilla registration/signup.html para esta vista.
    template_name='registration/signup.html'

    def get_success_url(self):
        # Devolver la URL de la vista de inicio de sesión con una cadena de consulta.
        return reverse_lazy('login') + '?register'
    
    
    # Si no se especifica la clase de formulario, la clase de formulario se establece en la clase de
    # formulario del modelo.  
    def get_form(self, form_class=None):
        
        # Llamar al método get_form de la clase principal (CreateView) y pasarle el parámetro
        # form_class.
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contrasena'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite Contrasena'})

        return form


# Este es un decorador que se utiliza para comprobar si el usuario ha iniciado sesión. Si el usuario
# no ha iniciado sesión, lo redirigirá a la página de inicio de sesión.
@method_decorator(login_required, name='dispatch')
# Esta clase es una subclase de UpdateView, que es una subclase de FormView, que es una subclase de
# TemplateResponseMixin, que es una subclase de ContextMixin, que es una subclase de View
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # Este es un atajo para obtener el objeto Perfil para el usuario actual. Si el objeto no
        # existe, se creará.
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form