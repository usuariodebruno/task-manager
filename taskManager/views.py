from django.shortcuts import render, redirect
from django.views import View

from django.contrib import messages

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
    def index(self, request):
        return render(request, 'taskManager/index.html')