from django import forms
from .models import *
from .forms import *
    
class taskDao:
    def registerTask(self, resquet, user):        
        form = TaskForm(resquet.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            self.save(form.cleaned_data, user)
            return task
        
    def ListTask(self, member):      
        return Task.objects.filter(user=member)
            
    def save(self, cleaned_data, u):
        title = cleaned_data['title']
        description = cleaned_data['description']

        task = Task.objects.create(
            title=title,
            description=description,
            user=u,
        )
        return task