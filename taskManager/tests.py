from django.test import TestCase, Client
from django.contrib.auth.models import User

from .forms import TaskForm
from .models import Task, Member

class RegisterTaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('teste_nome', 'teste@email.com', 'senha123')
        self.member = Member.objects.create(user=self.user)        
        self.client.login(username='teste_nome', password='senha123')

        self.valid_task_data = {
            'title': 'Tarefa Teste',
            'description': 'Essa é um descrição teste para uma tarefa.'
        }
        
    def test_post_registers_task_with_valid_data(self):
        response = self.client.post('/postRegisterTask/', self.valid_task_data)

        # Checagem
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/listTask/')

        created_task = Task.objects.get(title=self.valid_task_data['title'], user=self.user)
        self.assertEqual(created_task.description, self.valid_task_data['description'])

class ListTaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('teste_nome', 'teste@email.com', 'senha123')
        
    def test_get_list_tasks_view(self):
        client = Client()  # cliente de teste  
        client.force_login(self.user)  # forçar o login

        task1 = Task.objects.create(title='Tarefa 1', description='Descrição da Tarefa 1', user=self.user)
        task2 = Task.objects.create(title='Tarefa 2', description='Descrição da Tarefa 2', user=self.user)
        
        response = client.get('/listTask/')
       
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskManager/listTask.html')  
        self.assertQuerysetEqual(response.context['tasks'], [task1, task2], ordered=False)