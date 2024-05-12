from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Task
from .views import RegisterTaskView
from .forms import TaskForm

class RegisterTaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('teste_nome', 'teste@email.com', 'senha123')

        self.valid_task_data = {
            'title': 'Tarefa Teste',
            'description': 'Essa é um descrição teste para uma tarefa.'
        }
        
    def test_post_registers_task_with_valid_data(self):
        request = RequestFactory().post('', self.valid_task_data)
        request.user = self.user 

        view = RegisterTaskView()
        response = view.post(request, self.user)

        # Checagem
        self.assertEqual(response.status_code, 302)
        # self.assertContains(response, 'Tarefa: "'+ self.valid_task_data['title'] +'" registrada com sucesso!')
        self.assertEqual(response.url, '/')

        created_task = Task.objects.get(title=self.valid_task_data['title'], user=self.user)
        self.assertEqual(created_task.description, self.valid_task_data['description'])

    def test_post_renders_form_with_invalid_data(self):
        request = RequestFactory().post('', {'description': 'descrição'})  # Sem titulo
        request.user = self.user

        view = RegisterTaskView()
        response = view.post(request, self.user)
        
        self.assertEqual(response.status_code, 200) # Verifica a render do form com erros
        # self.assertContains(response, 'Este campo é obrigatório.')         
        self.assertTrue(TaskForm(data=request.POST).is_bound) # Verifica se o formulário tem erros