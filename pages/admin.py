from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    # Diciéndole a Django que muestre el título y el orden de la página en la página de
    # administración.
    list_display = ('title', 'order')
   # Le dice a Django que cargue el archivo custom_ckeditor.css 
   # cuando se procesa el widget CKEditor
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

# Registrando el modelo de página con la clase PageAdmin.
admin.site.register(Page, PageAdmin)




