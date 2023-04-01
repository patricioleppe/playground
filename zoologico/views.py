from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Animal
from .forms import AnimalForm

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

class AnimalListView(ListView):
    model = Animal
   

class AnimalDetailView(DetailView):
    model = Animal

@method_decorator(staff_member_required, name='dispatch')
class AnimalCreate(CreateView):
    # Diciéndole a Django que el modelo que se utilizará para esta vista es el modelo de página.
    model = Animal
    # Diciéndole a Django que el formulario que se usará para esta vista es el PageForm.
    form_class = AnimalForm
    # Diciéndole a Django que redirija a la vista de lista de páginas después de eliminar la página.
    success_url = reverse_lazy('animals')

    def dispatch(self, request, *args, **kwargs):            
        return super(AnimalCreate, self).dispatch(request, *args, **kwargs )
