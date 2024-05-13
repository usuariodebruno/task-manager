from django.shortcuts import render, redirect
from django.views import View

from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import *
from .forms import *
from .dao import *

class RegisterTaskView(View):
    def post(self, request, user):
        if request.method == 'POST':            
            dao = taskDao()
            task = dao.registerTask(request, user)
            if task:                
                #messages.success(request, 'Tarefa: "'+ task.title +'" registrada com sucesso!')
                return redirect('taskManager:index')
            
        form = TaskForm()
        #messages.error(request, 'Este campo é obrigatório.')
        return render(request, 'taskManager/registerTask.html', {'form': form})

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
                return render(request, 'taskManager/registerTask.html')
            else:  
                context = {
                    'mensagem': messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.'),
                }
                return render(request, 'taskManager/index.html', context)        
        return render(request, 'taskManager/index.html')