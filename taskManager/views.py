from django.shortcuts import render, redirect
from django.views import View

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .dao import *

class RegisterTaskView(View):    
    @login_required(redirect_field_name='next', login_url="/login/")
    def post(request):
        if request.method == 'POST':            
            dao = taskDao()
            task = dao.registerTask(request, request.user)
            if task:                
                messages.success(request, 'Tarefa: "'+ task.title +'" registrada com sucesso!')
                return redirect('taskManager:listTasks')
        messages.error(request, 'Este campo é obrigatório.')
        return RegisterTaskView.get(request)
    
    @login_required(redirect_field_name='next', login_url="/login/")
    def get(request):    
        form = TaskForm()        
        return render(request, 'taskManager/registerTask.html', {'form': form})

class ListTaskView(View):    
    @staticmethod
    @login_required(redirect_field_name='next', login_url="/login/")
    def get(request):           
        dao = taskDao()
        tasks = dao.ListTask(request.user)
        context = {
            'tasks': tasks 
        }
        return render(request, 'taskManager/listTask.html', context)

class GenericView(View):
    def index(request):
        return render(request, 'taskManager/index.html')
    
    def login(request):  
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')      
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  
                return redirect('taskManager:listTasks')
            else:  
                context = {
                    'mensagem': messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.'),
                }
                return render(request, 'taskManager/index.html', context)        
        return render(request, 'taskManager/index.html')