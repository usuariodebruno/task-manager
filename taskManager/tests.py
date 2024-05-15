from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from taskManager.models import Task, Member

class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('teste_nome', 'teste@email.com', 'senha123')
        self.member = Member.objects.create(user=self.user)
        self.client = Client()
        self.client.force_login(self.user)
        self.valid_task_data = {
            'title': 'Tarefa Teste',
            'description': 'Essa é um descrição teste para uma tarefa.'
        }
        self.task1 = Task.objects.create(title='Tarefa 1', description='Descrição da Tarefa 1', member=self.member)
        self.task2 = Task.objects.create(title='Tarefa 2', description='Descrição da Tarefa 2', member=self.member)

class RegisterTaskViewTest(BaseTest):
    def test_post_registers_task_with_valid_data(self):
        response = self.client.post('/postRegisterTask/', self.valid_task_data)

        # Checagem
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/listTask/')

        created_task = Task.objects.get(title=self.valid_task_data['title'], member=self.member)
        self.assertEqual(created_task.description, self.valid_task_data['description'])

class ListTaskViewTest(BaseTest):
    def test_get_list_tasks_view(self):
        response = self.client.get('/listTask/')
       
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskManager/listTask.html')  
        self.assertQuerysetEqual(response.context['tasks'], [self.task1, self.task2], ordered=False)

class DeleteTaskViewTest(BaseTest):
    def test_delete_task_view_success(self):
        response = self.client.post(reverse('taskManager:deleteTask', kwargs={'taskID': self.task1.id}))
        
        # checa se a tarefa foi excluida
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task1.id)
        
        # checa o redirecionamento
        self.assertRedirects(response, reverse('taskManager:listTasks'))
        
        self.assertEqual(response.status_code, 302) # redirecionar após a atualização

        # checa mensagens de sucesso na exclusão
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Tarefa excluida com sucesso!')

class UpdateTaskViewTestCase(BaseTest):
    def test_update_task_view(self):
        response = self.client.get(reverse('taskManager:updateTask', kwargs={'taskID': self.task1.id}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('taskManager:updateTask', kwargs={'taskID': self.task1.id}), {
            'title': 'Atualiza tarefa',
            'description': 'Atualiza descração',
            'completed': True
        })
        self.assertEqual(response.status_code, 302)  # redirecionar após a atualização
        self.assertRedirects(response, reverse('taskManager:listTasks'))

        # chega se a tarefa foi atualizada corretamente na base de dados
        updated_task = Task.objects.get(id=self.task1.id)
        self.assertEqual(updated_task.title, 'Atualiza tarefa')
        self.assertEqual(updated_task.description, 'Atualiza descração')
        self.assertTrue(updated_task.completed)
