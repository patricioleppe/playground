from django.test import TestCase, Client
from .models import Page
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.

class TestListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.page = Page.objects.create(title='Pagina de prueba', content='Esta es mi pagina de prueba', order=0)
        self.client = Client()        
        self.url = reverse('pages:pages')


    def test_pages_con_usuario_autenticado(self):
        
        self.client.login(username='testuser', password='password')
        # Envía la petición GET a la vista
        response = self.client.get(self.url)
        # Verifica que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        # Verifica que se esté usando la plantilla correcta
        self.assertTemplateUsed(response, 'miapp/mi_template.html')
        # Verifica que el contexto contenga el objeto necesario
        self.assertIn('mi_modelo', response.context)
        self.assertEqual(response.context['mi_modelo'], self.mi_modelo)