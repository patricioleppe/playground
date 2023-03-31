from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.usr = User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_user_exist(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)

    def test_user_delete(self):
        user = User.objects.delete(user= 'test')
        user.delete()
        self.assertEqual(user, False)
          

# class TestListView(TestCase):
    
#         self.user = User.objects.create_user(username='testuser', password='password')
#         self.page = Page.objects.create(title='Pagina de prueba', content='Esta es mi pagina de prueba', order=0)
#         self.client = Client()        
#         self.url = reverse('pages:pages')


#     def test_pages_con_usuario_autenticado(self):
        
#         self.client.login(username='testuser', password='password')
#         # Envía la petición GET a la vista
#         response = self.client.get(self.url)
#         # Verifica que la respuesta sea exitosa
#         self.assertEqual(response.status_code, 200)
#         # Verifica que se esté usando la plantilla correcta
#         self.assertTemplateUsed(response, 'miapp/mi_template.html')
#         # Verifica que el contexto contenga el objeto necesario
#         self.assertIn('mi_modelo', response.context)
#         self.assertEqual(response.context['mi_modelo'], self.mi_modelo)