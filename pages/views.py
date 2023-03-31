from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm


# class StaffRequiredMixin(object):
#     """Este mixin requerira que el usuario sea miembro del stafff"""

#     # Un decorador que se utiliza para verificar si el 
#     # usuario es un miembro del personal.
#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         # if not request.user.is_staff:
#         #     # Redirigir al usuario a la página de inicio de sesión del administrador.
#         #     return redirect(reverse_lazy('admin:login'))
#         # Llamar al método de envío de la clase principal.
#         return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    

class PageListView(ListView):
    model = Page
   

class PageDetailView(DetailView):
    model = Page


# Un decorador que se utiliza para comprobar si el usuario es miembro del personal.
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    # Diciéndole a Django que el modelo que se utilizará para esta vista es el modelo de página.
    model = Page
    # Diciéndole a Django que el formulario que se usará para esta vista es el PageForm.
    form_class = PageForm
    # Diciéndole a Django que redirija a la vista de lista de páginas después de eliminar la página.
    success_url = reverse_lazy('pages:pages')

    def dispatch(self, request, *args, **kwargs):            
        return super(PageCreate, self).dispatch(request, *args, **kwargs )


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):  
        return reverse_lazy('pages:update', args = [self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')